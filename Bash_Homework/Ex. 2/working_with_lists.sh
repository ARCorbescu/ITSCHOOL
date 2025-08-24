#!/bin/bash

# Author: Corbescu Alexandru-Robert
# Date Created: 24/08/2025
# Last Modified: 24/08/2025
# Version: 1.0

# Description:
# It requires at least three numeric parameters.
# The script calculates and displays:
#   - The sum of all the numbers
#   - The arithmetic mean (average) of the numbers, with 3 decimal places

# Usage:
# ./directory_handler.sh <num1> <num2> <num3> [additional_numbers...]


# Test that the script received at least 3 params
if [ $# -lt 3 ]; then
    echo "Usage requires at least 3 paramets; Only $# were given"
    exit 1
fi

# Compute the sum of the numbers
SUM=0
for var in "$@"
do
    SUM=$((SUM + var))
done

echo "The sum of the numbers is: $SUM"
echo "The average of the numbers is: $(echo "scale=3; $SUM / $#" | bc)"
