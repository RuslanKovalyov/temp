# move files from given directory to another given directory one by one in a loop.

import os
import shutil
from pathlib import Path

# input source directory
source_dir = input("Enter the source directory: ")
# input destination directory
destination_dir = input("Enter the destination directory: ")

# get all files in the source directory
files = os.listdir(source_dir)

# loop through all files. Copy each file to the destination directory and remove original file one by one
for file in files:
    # get the file path
    file_path = os.path.join(source_dir, file)
    # copy the file to the destination directory
    shutil.copy(file_path, destination_dir)
    # remove the original file
    os.remove(file_path)
    print(f"File {file} moved to {destination_dir}")