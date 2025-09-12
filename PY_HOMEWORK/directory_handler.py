import sys
import os
from pathlib import Path

def with_try_catch(dir_path):
    try:
        dir_path = Path(sys.argv[1])
    except IndexError:
        print("Eroare: Nu a fost specificat niciun argument pentru director.")
        sys.exit(1)

    try:
        if Path.is_dir(dir_path):
            print("Directorul exista iar el contine:")
            try:
                files = [
                    (file.name, "File size is: " + str(format(os.path.getsize(file), '.2f') + " KB"))
                    for file in dir_path.iterdir() if file.is_file()
                ]
                if files:
                    print(*files, sep='\n')
                else:
                    print("Nu Contine Nimic")
            except Exception as e:
                print(f"Eroare la listarea fisierelor: {e}")
        else:
            try:
                Path(dir_path).mkdir(parents=True, exist_ok=True)
                print(f"The directoy was created: {dir_path}")
            except Exception as e:
                print(f"Eroare la crearea directorului: {e}")
    except Exception as e:
        print(f"Eroare generala: {e}")

if __name__ == "__main__":
    # Get the directory path from command line arguments
    dir_path = Path(sys.argv[1])

    # Check if the directory exists
    if Path.is_dir(dir_path):
        print("The directory exists and contains:")
        # Create a list of files in the directory with their sizes in KB
        files = [
            (file.name, "File size is: " + str(format(os.path.getsize(file), '.2f') + " KB"))
            for file in dir_path.iterdir() if file.is_file()
        ]
        # Print the files or a message if the directory is empty
        if files:
            print(*files, sep='\n')
        else:
            print("Directory is empty")
    else:
        # Create the directory if it does not exist
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"The directory was created: {dir_path}")