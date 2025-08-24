#!/bin/bash

# Author: Corbescu Alexandru-Robert
# Date Created: 24/08/2025
# Last Modified: 24/08/2025

# Description
# The script receives a directory path as an argument
# If that path points to a valid directory it lists all files and directories with their sizes.
# If the path is invalid or not a directory, it creates a directory at that path and logs a meesage.

# Usage
# directory_handler.sh <directory_path>

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

DIR_PATH="$1"

if [[ -d $DIR_PATH ]]; then
    echo "Displaing the files inside the directory in orted by size"
    ls -l $DIR_PATH/ | sort -rh
else
    echo "Creating the directory at: $1"
    mkdir $1
fi
