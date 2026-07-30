import os

import cffi
import pytest

ffi = cffi.FFI()
from cffi import FFI

# Ensure ffi is available for string conversions
ffi = FFI()


@pytest.mark.bonus
def test_multiple_fds_alternating(lib_bonus, tmp_path):
    """Test alternating reads between two file descriptors."""
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("1_A\n1_B\n1_C\n")
    file2.write_text("2_A\n2_B\n2_C\n")

    fd1 = os.open(file1, os.O_RDONLY)
    fd2 = os.open(file2, os.O_RDONLY)

    try:
        # Interleave reads to ensure buffers don't mix
        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"1_A\n"
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"2_A\n"

        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"1_B\n"
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"2_B\n"

        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"1_C\n"
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"2_C\n"

        # Ensure both reach EOF cleanly
        assert lib_bonus.get_next_line(fd1) == ffi.NULL
        assert lib_bonus.get_next_line(fd2) == ffi.NULL
    finally:
        os.close(fd1)
        os.close(fd2)


@pytest.mark.bonus
def test_multiple_fds_sequential(lib_bonus, tmp_path):
    """Test reading one fd fully before starting another."""
    file1 = tmp_path / "seq1.txt"
    file2 = tmp_path / "seq2.txt"

    file1.write_text("File1_Line1\nFile1_Line2\n")
    file2.write_text("File2_Line1\nFile2_Line2\n")

    fd1 = os.open(file1, os.O_RDONLY)
    fd2 = os.open(file2, os.O_RDONLY)

    try:
        # Exhaust fd1 first
        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"File1_Line1\n"
        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"File1_Line2\n"
        assert lib_bonus.get_next_line(fd1) == ffi.NULL

        # Ensure fd2 is completely untouched and reads from the beginning
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"File2_Line1\n"
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"File2_Line2\n"
        assert lib_bonus.get_next_line(fd2) == ffi.NULL

        # Call fd1 again after EOF to ensure it doesn't crash or mix states
        assert lib_bonus.get_next_line(fd1) == ffi.NULL
    finally:
        os.close(fd1)
        os.close(fd2)


@pytest.mark.bonus
def test_three_fds_chaos(lib_bonus, tmp_path):
    """Test interleaved reads across three file descriptors randomly."""
    f1 = tmp_path / "chaos1.txt"
    f2 = tmp_path / "chaos2.txt"
    f3 = tmp_path / "chaos3.txt"

    f1.write_text("A1\nA2\nA3\n")
    f2.write_text("B1\nB2\nB3\n")
    f3.write_text("C1\nC2\nC3\n")

    fd1 = os.open(f1, os.O_RDONLY)
    fd2 = os.open(f2, os.O_RDONLY)
    fd3 = os.open(f3, os.O_RDONLY)

    try:
        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"A1\n"
        assert ffi.string(lib_bonus.get_next_line(fd3)) == b"C1\n"
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"B1\n"

        assert ffi.string(lib_bonus.get_next_line(fd3)) == b"C2\n"
        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"A2\n"
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"B2\n"

        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"A3\n"
        assert ffi.string(lib_bonus.get_next_line(fd3)) == b"C3\n"
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"B3\n"

        assert lib_bonus.get_next_line(fd1) == ffi.NULL
        assert lib_bonus.get_next_line(fd2) == ffi.NULL
        assert lib_bonus.get_next_line(fd3) == ffi.NULL
    finally:
        os.close(fd1)
        os.close(fd2)
        os.close(fd3)


@pytest.mark.bonus
def test_no_trailing_newline_interleaved(lib_bonus, tmp_path):
    """Test files without trailing newlines mixed with files that have them."""
    f1 = tmp_path / "no_nl.txt"
    f2 = tmp_path / "with_nl.txt"

    f1.write_text("Hello\nWorld")  # No trailing newline on the last line
    f2.write_text("Foo\nBar\n")  # Trailing newline

    fd1 = os.open(f1, os.O_RDONLY)
    fd2 = os.open(f2, os.O_RDONLY)

    try:
        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"Hello\n"
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"Foo\n"

        # Read the last line of fd1 (no newline)
        assert ffi.string(lib_bonus.get_next_line(fd1)) == b"World"
        assert lib_bonus.get_next_line(fd1) == ffi.NULL

        # Ensure fd2 still reads its remaining lines correctly
        assert ffi.string(lib_bonus.get_next_line(fd2)) == b"Bar\n"
        assert lib_bonus.get_next_line(fd2) == ffi.NULL
    finally:
        os.close(fd1)
        os.close(fd2)
