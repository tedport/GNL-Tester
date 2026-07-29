import pytest
import subprocess

BS_VALUE = "4096"

def pytest_addoption(parser):
    parser.addoption(
        "--bs", 
        action="store", 
        default="4096", 
        help="Buffer size for get_next_line"
    )
    parser.addoption(
        "--bonus",
        action="store_true",
        default=False,
        help="Test bonus for get_next_line"
	)

def pytest_configure(config):
    global BS_VALUE
    BS_VALUE = config.getoption("--bs")
    
    # Register the custom marker so pytest doesn't throw warnings
    config.addinivalue_line(
        "markers", "extra: mark test as part of the extra test suite"
    )

    target = "re"
    if config.getoption("--bonus"):
        target += "bonus"
    
    # Existing makefile compilation logic...
    print(f"\n[conftest] Compiling with make re BUFFER_SIZE={BS_VALUE}...")
    try:
        result = subprocess.run(
            ["make", "re", f"BUFFER_SIZE={BS_VALUE}"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(result.stdout)
            print(result.stderr)
            pytest.exit(f"\n[conftest] Makefile compilation failed! Aborting tests.")
        else:
            print("[conftest] Compilation successful.")
    except FileNotFoundError:
        pytest.exit("\n[conftest] 'make' command not found.")
