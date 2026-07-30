# gnlTester

A comprehensive, automated testing suite for the 42 `get_next_line` project. It uses `pytest` and `cffi` to dynamically compile your code with various `BUFFER_SIZE` configurations and rigorously test it against edge cases, pre-generated files, and randomized stress tests.

## Features

- **Dynamic Compilation:** Automatically compiles your code as a shared library (`.so`) for multiple `BUFFER_SIZE` values (`1`, `16`, `32`, `42`, `4096`, `8192`).
- **Extensive Coverage:** 
  - Invalid file descriptors.
  - Empty files, single lines, and huge lines.
  - Files with no trailing newlines, multiple consecutive newlines, and mixed lengths.
  - Dynamic randomized stress tests (hundreds of lines, varying lengths).
- **Bonus Support:** Rigorous testing for managing multiple file descriptors simultaneously (alternating, sequential, and chaotic interleaved reads).
- **Automated Cleanup:** Compiles and cleans up all temporary libraries automatically before and after the test session.

## Prerequisites

Ensure you have the following installed on your system:
- **Python 3.13+**
- **uv** (Fast Python package installer and resolver)
- **gcc** (C compiler)
- **make**

## Setup & Usage

1. **Clone the tester** inside your `get_next_line` project directory (where your `get_next_line.c` and header files are located):
   ```bash
   git clone https://github.com/tedport/gnlTester.git
   cd gnlTester
   ```

2. **Run the mandatory tests:**
   ```bash
   uv run pytest -s -v
   ```

3. **Run the bonus tests** (multiple file descriptors):
   ```bash
   uv run pytest -s -v --bonus
   ```

## Command Line Options

You can pass specific flags to `pytest` to customize your test run:

- `--bonus`: Enables the bonus test suite (testing multiple file descriptors simultaneously).
- `--project-path=<path>`: Specifies the relative path to your `get_next_line` source files. 
  - *Default:* `..` (assumes the tester is cloned directly inside your project folder).
  - *Example:* `uv run pytest -s -v --project-path=../path/to/my_gnl`

## How It Works

1. **Configuration (`conftest.py`):** When `pytest` starts, it reads your `get_next_line.h` file using `cffi` to understand the struct definitions and function signatures.
2. **Compilation (`Makefile`):** It invokes `make` to compile your C code into shared libraries (`libgnl_<BUFFER_SIZE>.so`). The `AUTHORIZED_INVOKER=1` flag is passed to bypass the manual-execution safety check in the Makefile.
3. **Execution:** The tests open file descriptors (both pre-generated static files in `tests/files/` and dynamically generated temporary files) and assert that `get_next_line` returns the exact expected strings.
4. **Cleanup:** After all tests finish, `pytest` automatically runs `make fclean` to remove the compiled `.so` files.

## Project Structure
```
gnlTester/
├── Makefile                 # Handles dynamic .so compilation
├── pyproject.toml           # Python dependencies (pytest, cffi)
├── README.md                # This file
└── tests/
    ├── conftest.py          # Pytest config, fixtures, and C compilation logic
    ├── random_data_provider.py # Script to generate random ASCII test files
    ├── test_gnl.py          # Mandatory test suite
    ├── test_gnl_bonus.py    # Bonus test suite (multiple FDs)
    └── files/               # Pre-generated static test files