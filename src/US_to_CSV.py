import os
import csv
from tqdm import tqdm

# You are not supposed to change these variables just put your USs as text files in `data/All_US` folder
#   and then run the script you will find the csv file in `data/All_US.csv`
folder_path = "./data/All_US"
output_file_path = "./data/All_US.csv"

File_Counter = 0
Total_lines = 0 
with open(output_file_path, 'w', newline='') as output_file:
    # if the output file exists make it empty if it does not exist create an empty file
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['File No.', 'File Name', 'No. of line', 'Project Name', 'User Story'])

    # Loop through all files in the folder in in the ./data folder
    for filename in tqdm(os.listdir(folder_path)):
        file_path = os.path.join(folder_path, filename)
        # Check if the item is a file (not a subdirectory)
        if os.path.isfile(file_path):
            Line_Counter = 0
            File_Counter += 1
            #print(f'Reading content from file: {filename}.\n So far the tool read {File_Counter} files.')

            # Find Project name from file name
            Project_Name = filename.replace(".txt", "")
            Project_Name = Project_Name.split('-', 1)[-1]
            Project_Name = Project_Name.replace("User Stories for", "").strip()
            #print(Project_Name)


            # Open the file 
            with open(file_path, 'r', encoding='ISO-8859-1') as file:
                
                # Read the content of the file
                file_lines = file.readlines()

                #Write the content of the file to the output file
                file_content_list = list()
                # print(f'\nReading content from file: {filename}.')
                for line in file_lines:
                    if line.strip() == "":
                        continue
                    line = line.rstrip('\n')
                    Line_Counter += 1
                    file_content_list.append([File_Counter, filename, Line_Counter, Project_Name, line])
                # print(f"There was {Line_Counter} in {filename}")
                csv_writer = csv.writer(output_file)
                csv_writer.writerows(file_content_list)
            Total_lines += Line_Counter


print(f'\nThe tool found {File_Counter} files and found {Total_lines} User Stories in total.')