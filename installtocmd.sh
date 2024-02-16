#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Directory containing the script to be copied
SOURCE_DIR="$SCRIPT_DIR"

# Name of the script to be copied
SCRIPT_NAME="pynova.py"

# Directory in PATH where the script will be copied
TARGET_DIR="/usr/local/bin"

# Check if the script exists and is executable
if [ ! -x "$SOURCE_DIR/$SCRIPT_NAME" ]; then
    echo "Error: Script is not executable or does not exist: $SOURCE_DIR/$SCRIPT_NAME"
    exit 1
fi

# Copy script to target directory, override if it already exists
cp -f "$SOURCE_DIR/$SCRIPT_NAME" "$TARGET_DIR/pynova"

# Ensure copy was successful
if [ $? -eq 0 ]; then
    echo "Script copied to PATH: $TARGET_DIR"
else
    echo "Error copying script to PATH: $TARGET_DIR"
    exit 1
fi
