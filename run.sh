#!/bin/sh
# run.sh - Cross-platform (Linux/macOS) script to start SchindlersShoppingList

# Exit on error
set -e

# Find Python (prefer python3, fallback to python)
PYTHON_BIN=""
if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
else
    echo "Python is not installed. Please install Python 3.x." >&2
    exit 1
fi

# Optionally activate a virtual environment if present
if [ -f "venv/bin/activate" ]; then
    . venv/bin/activate
fi

# Run the main application
$PYTHON_BIN app.py "$@"
