#!/bin/bash

# Author: Corbescu Alexandru-Robert
# Date Created: 24/08/2025
# Last Modified: 24/08/2025

# Description:
# This script checks the state of a given systemd service.
# - If the service is active, it simply reports the status.
# - If the service is inactive, the user is prompted whether to start it.
# - If the user accepts, the script starts the service.
# - If the user declines, the script exits without starting the service.

# Usage:
# ./service_handler.sh <service_name>

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
        systemctl start $1
    else
        echo "The service will remain $SERVICE_STATE"
        exit 0
    fi
fi
