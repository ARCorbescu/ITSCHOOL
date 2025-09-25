import os
import sys
from pathlib import Path
import subprocess

def get_dir_size_in_bytes(dir_path):
    # Check if the provided path is a directory
    if not dir_path.is_dir():
        raise Exception(f'Directory does not exist at path: {dir_path}')
    
    # Get the size of the directory in bytes using 'du' and 'awk'
    # Example output: b'10799848\t/home/arccorbescu/work/ITSCHOOL/ITSCHOOL\n'
    result = str(subprocess.check_output(f'du -sb "{dir_path}" | awk "{{print $1}}"', shell=True))
    
    # Extract the size as an integer from the command output
    # Example: 10799852
    return int(result.split('\\')[0][2:])


def get_total_partition_size(dir_path):
    # Get the total size of the partition containing the directory using 'df' and 'awk'
    # Example output: b'981132795904\n'
    result = str(subprocess.check_output(f"df --block-size=1 {dir_path} | awk 'NR==2 {{print $2}}'", shell=True))
    # Extract the partition size as an integer from the command output
    # Example: 981132795904
    return int(result[2:-3])


if __name__ == "__main__":
    # Get the directory path from command line arguments
    dir_path = Path(sys.argv[1])

    # Calculate the directory size and partition size
    dir_size = get_dir_size_in_bytes(dir_path)
    disk_size = get_total_partition_size(dir_path)

    # Calculate the usage percentage
    percentage = float(format(dir_size * 100 / disk_size, '.2f'))
    print(percentage)

    # Print an alert if usage exceeds 5%
    if percentage >= 5.0:
        print("⚠️ Alert: Directory usage exceeds 5% of the partition!")
    else:
        print(f"All good dir uses {percentage} of the partition")


"""
import sys
import argparse
from pathlib import Path
import subprocess

def get_dir_size_in_bytes(dir_path):
    # Check if the provided path is a directory
    if not dir_path.is_dir():
        raise Exception(f'Directory does not exist at path: {dir_path}')
    try:
        # Get the size of the directory in bytes using 'du' and 'awk'
        result = subprocess.check_output(
            f'du -sb "{dir_path}" | awk "{{print $1}}"', shell=True, text=True
        )
        return int(result.strip())
    except Exception as e:
        raise RuntimeError(f"Failed to get directory size: {e}")

def get_total_partition_size(dir_path):
    try:
        # Get the total size of the partition containing the directory using 'df' and 'awk'
        result = subprocess.check_output(
            f"df --block-size=1 {dir_path} | awk 'NR==2 {{print $2}}'", shell=True, text=True
        )
        return int(result.strip())
    except Exception as e:
        raise RuntimeError(f"Failed to get partition size: {e}")

if __name__ == "__main__":
    # Parse command line arguments for directory and threshold
    parser = argparse.ArgumentParser(description="Check directory disk usage as a percentage of its partition.")
    parser.add_argument("directory", type=str, help="Path to the directory to check.")
    parser.add_argument("--threshold", type=float, default=5.0, help="Alert threshold percentage (default: 5.0)")
    args = parser.parse_args()

    dir_path = Path(args.directory)
    dir_size = get_dir_size_in_bytes(dir_path)
    disk_size = get_total_partition_size(dir_path)

    # Calculate and print the usage percentage
    percentage = round(dir_size * 100 / disk_size, 2)
    print(f"Directory usage: {percentage}%")

    # Print an alert if usage exceeds the threshold
    if percentage >= args.threshold:
        print(f"⚠️ Alert: Directory usage exceeds {args.threshold}% of the partition!")
"""