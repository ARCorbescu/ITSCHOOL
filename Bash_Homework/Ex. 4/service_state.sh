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
    echo "Usage: $0 <service_name>"
    exit 1
fi

SERVICE_STATE=$(systemctl is-active $1)
echo "The current state of the "$1" service is: $SERVICE_STATE"

if [ $SERVICE_STATE != "active" ]; then
    read -p "Would you like to start the service? y/n: " ANSWER
    if [ $ANSWER == "y" ] || [ $ANSWER == "Y" ]; then
        echo "The service $1 will be started..."
        sudo systemctl start ssh
    else
        echo "The service will remain $SERVICE_STATE"
        exit 0
    fi
fi
