import os
import subprocess
from contextlib import contextmanager

import pytest
from cffi import FFI

BUFFER_SIZE_VALUES = ["1", "16", "32", "42", "4096", "8192"]
PROJECT_ROOT = ""

# __file__ is tests/conftest.py
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
# TESTER_ROOT is the parent directory (where your Makefile lives)
TESTER_ROOT = os.path.dirname(TEST_DIR) 


def pytest_addoption(parser):
    parser.addoption(
        "--project-path",
        action="store",
        default="..", # Points to the C project root (sibling to tester root)
        help="Path to the project directory",
    )
    parser.addoption(
        "--bonus",
        action="store_true",
        default=False,
        help="Test bonus for get_next_line",
    )


def pytest_sessionfinish(session, exitstatus):
    # Use TESTER_ROOT to find the Makefile
    print(f"[INFO] Cleaning up compiled libraries in {TESTER_ROOT}...", flush=True)
    try:
        subprocess.run(
            ["make", "fclean", "AUTHORIZED_INVOKER=1"],
            check=False,
            cwd=TESTER_ROOT,  # <--- CHANGED to TESTER_ROOT
            capture_output=True,
            text=True,
        )
        print("[INFO] Cleanup successful.", flush=True)
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] Could not run make fclean. {e}", flush=True)


def pytest_configure(config):
    global PROJECT_ROOT
    config.addinivalue_line("markers", "bonus: bonus part of the project test")
    PROJECT_ROOT = os.path.abspath(config.getoption("--project-path"))

    lib_targets = [
        *[(bs, f"libgnl_{bs}.so") for bs in BUFFER_SIZE_VALUES],
    ]
    if config.getoption("--bonus"):
        lib_targets.append((BUFFER_SIZE_VALUES[-1], "libgnl_bonus.so"))
        
    for bs, target in lib_targets:
        print(f"[INFO] Compiling {target} (BUFFER_SIZE={bs})...", flush=True)
        result = subprocess.run(
            [
                "make",
                f"NAME={target}",
                f"PROJECT_PATH={PROJECT_ROOT}",
                f"BUFFER_SIZE={bs}",
                "AUTHORIZED_INVOKER=1"
            ],
            capture_output=True,
            text=True,
            cwd=TESTER_ROOT,  # <--- CHANGED to TESTER_ROOT
            check=False,
        )
        if result.returncode != 0:
            print(f"[ERROR] Compilation failed for {target}:\n{result.stderr}", flush=True)
            pytest.exit(f"Compilation failed for {target}:\n{result.stderr}")
        else:
            print(f"[INFO] {target} has compiled successfully.\n{result.stdout}", flush=True)


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--bonus"):
        skip_bonus = pytest.mark.skip(reason="needs --bonus option to run")
        for item in items:
            if "bonus" in item.keywords:
                item.add_marker(skip_bonus)


def load_lib(libname: str, bs: int):
    ffi = FFI()

    header = os.path.join(PROJECT_ROOT, "get_next_line.h")
    try:
        with open(header, "r") as h:
            header_content = h.read().replace("BUFFER_SIZE", str(bs))
    except FileNotFoundError:
        print(f"[ERROR] Header not found at {header}!", flush=True)
        pytest.fail(f"Header not found at {header}!")

    cdef_str = "\n".join(
        line for line in header_content.splitlines() if not line.strip().startswith("#")
    )
    ffi.cdef(cdef_str)
    
    # The .so files are compiled into TESTER_ROOT by the Makefile
    lib_path = os.path.join(TESTER_ROOT, libname)  # <--- CHANGED to TESTER_ROOT
    return ffi, ffi.dlopen(lib_path)


@pytest.fixture(params=BUFFER_SIZE_VALUES, scope="session")
def lib(request):
    bs = request.param
    _, C = load_lib(f"libgnl_{bs}.so", bs)
    yield C


@pytest.fixture(params=BUFFER_SIZE_VALUES, scope="session")
def lib_bonus(request):
    bs = request.param
    _, C = load_lib("libgnl_bonus.so", bs)
    yield C


# If you moved `files/` inside `tests/`, this stays as TEST_DIR.
# If you kept `files/` in the root, change this to TESTER_ROOT.
FILES_DIR = os.path.join(TEST_DIR, "files")

@contextmanager
def open_gnl_file(filename):
    """Helper to handle file opening and closing automatically."""
    fd = os.open(os.path.join(FILES_DIR, filename), os.O_RDONLY)
    try:
        yield fd
    finally:
        os.close(fd)