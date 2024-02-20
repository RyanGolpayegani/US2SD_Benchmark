import os
import shutil

# Source and destination folders
source_folder = "SD/SDt"
destination_folder = "SD/SDi"
text_files_list = [file for file in os.listdir(source_folder) if file.endswith(".txt")]

os.makedirs(destination_folder, exist_ok=True)

# Generate diagrams using the PlantUML command
for SDt in os.listdir(source_folder):
    file_name = f"SD/SDt/{SDt}"
    os.system(f"python -m plantuml {file_name}")

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

print("Image generation was successful.")
