import os
import shutil

def rename_files_by_creation_date(folder_path):
    # Get all files in the folder
    files = os.listdir(folder_path)
    
    # Create a list of tuples containing filename and creation time
    file_info_list = [(file, os.path.getctime(os.path.join(folder_path, file))) for file in files]
    
    # Sort the list based on creation time
    file_info_list.sort(key=lambda x: x[1])
    
    # Iterate over the sorted list and rename files
    for index, (file_name, _) in enumerate(file_info_list):
        # Extract file extension
        file_name_without_ext, file_ext = os.path.splitext(file_name)
        
        # Create a new filename based on creation order
        new_file_name = f"{index+1:03d}_{file_name_without_ext}{file_ext}"
        
        # Rename the file
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
        
        print(f"Renamed {file_name} to {new_file_name}")

# Example usage:
folder_path = "/student/nwh714/WORKDIR/US2SD_Benchmark/Experiment/US T5/Full_A_GPT"
# folder_path = "/student/nwh714/WORKDIR/US2SD_Benchmark/Experiment/US T5/SDi"
# folder_path = "/student/nwh714/WORKDIR/US2SD_Benchmark/Experiment/US T5/SDt"
# folder_path = "/student/nwh714/WORKDIR/US2SD_Benchmark/Experiment/US T5/Selected_USs"

rename_files_by_creation_date(folder_path)
