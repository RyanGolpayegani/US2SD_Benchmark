import openai
import pandas as pd
from datetime import datetime
import os
from tqdm import tqdm

# Number_of_SDs += 1
Engine_model = "gpt-4"

# Specify the paths for the original and copy CSV files
CSV_file = "data/All_US.csv"

# Set up the OpenAI API clientexplain the moon landing to a 6 years old in a few sentence
openai.api_key = input('Enter API key: ')

# Read USs and select N random US 
All_Data = pd.read_csv(CSV_file)


project_names = All_Data['Project Name'].unique()
for project in tqdm(project_names):
    combined_string = All_Data.loc[All_Data['Project Name'] == project, 'User Story'].str.cat(sep=', ')
    # Generate a response
    prompt = combined_string
    print(project)

    # Call GPT API
    completion = openai.chat.completions.create(
            model = Engine_model,
            messages = [
                {
                    "role" : "user",
                    "content": prompt,
                }
            ]
        )
    gpt_full_answer = completion.choices[0].message.content
   
    

    # Create the destination folder if it doesn't exist
    Full_A_Folder_Project_Descriptions_dir = "data/Project_Descriptions/GPT4" 
    Full_A_File_Project_Descriptions_dir = f"data/Project_Descriptions/GPT4/{project}.txt" 

    # Full_A_Folder_Project_Descriptions_dir = "data/Project_Descriptions/GPT4" 
    # File_Project_Descriptions_dir = f"data/Project_Descriptions/GPT4/{project}.txt" 

    if not os.path.exists(Full_A_Folder_Project_Descriptions_dir):
        os.makedirs(Full_A_Folder_Project_Descriptions_dir)

    with open(Full_A_File_Project_Descriptions_dir, "w") as prj_desc_file:
        prj_desc_file.write(gpt_full_answer)

