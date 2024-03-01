import os
import shutil

# Specify the directory path
directory_path = "SD"

# Get a list of all items (directories and files) in the directory
all_items = os.listdir(directory_path)

# Filter out directories from the list of items
directories = [item for item in all_items if os.path.isdir(os.path.join(directory_path, item))]

# Sort the list of directories based on creation time (latest first)
directories.sort(key=lambda x: os.path.getctime(os.path.join(directory_path, x)), reverse=True)

# Get the latest created folder
latest_folder = directories[0] if directories else None

print("Latest created folder:", latest_folder)

# Source and destination folders
source_folder = f"SD/{latest_folder}/SDt"
destination_folder = f"SD/{latest_folder}/SDi"
text_files_list = [file for file in os.listdir(source_folder) if file.endswith(".txt")]

# Iterate through all files in the directory
for filename in os.listdir(source_folder):
    # Check if the file is a text file (ends with .txt)
    if filename.endswith(".txt"):
        # Check if the filename contains a space
        if " " in filename:
            # Replace the space with underscore
            new_filename = filename.replace(" ", "_")
            # Construct the old and new file paths
            old_filepath = os.path.join(source_folder, filename)
            new_filepath = os.path.join(source_folder, new_filename)
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed {filename} to {new_filename}")


os.makedirs(destination_folder, exist_ok=True)
# print(os.listdir(source_folder))
# Generate diagrams using the PlantUML command
for SDt in os.listdir(source_folder):
    file_name = f"SD/{latest_folder}/SDt/{SDt}"
    os.system(f"python -m plantuml {file_name}")
    # print(file_name)

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List all files in the source folder
files = os.listdir(source_folder)

# Iterate over each file
for file in files:
    # Check if the file is a PNG file
    if file.endswith(".png"):
        # Construct the full paths for source and destination
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        
        # Move the file to the destination folder
        shutil.move(source_path, destination_path)
