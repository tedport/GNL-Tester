import os
import tempfile
import pytest
from cffi import FFI
import conftest

HEADER_PATH = "../get_next_line.h"

bs_value = conftest.BS_VALUE

try:
    with open(HEADER_PATH, "r") as f:
        header_content = f.read()
except FileNotFoundError:
    pytest.fail(f"Header file not found at '{HEADER_PATH}'. Please update HEADER_PATH.")

header_content = header_content.replace("BUFFER_SIZE", bs_value)

cdef_string = "\n".join(
    line for line in header_content.splitlines() if not line.strip().startswith("#")
)

ffi = FFI()
ffi.cdef(cdef_string)

@pytest.fixture(scope="session")
def lib():
    """Loads the shared library."""
    lib_name = "../libgnl.so"
    lib_path = os.path.abspath(lib_name)
    
    if not os.path.exists(lib_path):
        pytest.fail(f"Shared library not found at {lib_path}. Did you compile it?")
        
    return ffi.dlopen(lib_path)

def test_get_next_line(lib):
    content = b"line1\nline2\nline3_no_newline"
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        fd = os.open(tmp_path, os.O_RDONLY)
        print(fd, tmp_path)
        
        line1 = lib.get_next_line(fd)
        assert line1 != ffi.cast(ffi.BVoidP, 0)
        assert ffi.string(line1) == b"line1\n"
        
        line2 = lib.get_next_line(fd)
        assert ffi.string(line2) == b"line2\n"
        
        line3 = lib.get_next_line(fd)
        assert ffi.string(line3) == b"line3_no_newline"
        
        line4 = lib.get_next_line(fd)
        assert line4 == ffi.NULL
        
        os.close(fd)
    finally:
        os.remove(tmp_path)
        pass
