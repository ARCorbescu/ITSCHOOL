#!/bin/bash

# Author: Corbescu Alexandru-Robert
# Date Created: 25/08/2025
# Last Modified: 25/08/2025

# Description:
# This script checks the state of a given systemd service.
# - If the service is active, it simply reports the status.
# - If the service is inactive, the user is prompted whether to start it.
# - If the user accepts, the script starts the service.
# - If the user declines, the script exits without starting the service.

# Usage:
# ./disk_usage_alert.sh <service_name>

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

# Get directory size (bytes)
DIR_SIZE=$(du -sb "$1" | awk '{print $1}')

# Get total partition size (bytes) for the filesystem where the directory resides
TOTAL_SIZE=$(df --block-size=1 "$1" | awk 'NR==2 {print $2}' )

# Compute percentage (with 2 decimal places)
PERCENTAGE=$(($DIR_SIZE * 100 / $TOTAL_SIZE))
PERCENTAGE_FLOAT=$(echo "scale=2; $DIR_SIZE * 100 / $TOTAL_SIZE" | bc)

echo "The size of the directory in bytes is:" $DIR_SIZE
echo "The total disk space on the machine is:" $TOTAL_SIZE
echo "The percentage used by $1 is:" $PERCENTAGE "(truncated)"

# Alert if > 5%
if [ $PERCENTAGE -gt 5 ]; then
    echo "⚠️ Alert: Directory usage exceeds 5% of the partition!"
fi