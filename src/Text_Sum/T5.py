from transformers import T5ForConditionalGeneration, T5Tokenizer
import pandas as pd
import os
from tqdm import tqdm

# Load T5 model and tokenizer
t5_model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base')

df = pd.read_csv("data/All_US.csv")

# Combine all values in 'col1' into a string with comma (,) separator
project_names = df['Project Name'].unique()

print(f"Generating description for all projects with T5...")

# for loop here
for project in tqdm(project_names):
    combined_string = df.loc[df['Project Name'] == project, 'User Story'].str.cat(sep=', ')

    # Tokenize input text
    inputs = tokenizer.encode("summarize: " + combined_string, return_tensors="pt", max_length=1024, truncation=True)

    # Generate summary using T5
    summary_ids = t5_model.generate(inputs, max_length=100, min_length=30, num_beams=4, early_stopping=True)

    # Decode summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Create the destination folder if it doesn't exist
    Folder_Project_Descriptions_dir = "data/Project_Descriptions/T5" 
    File_Project_Descriptions_dir = f"data/Project_Descriptions/T5/{project}.txt" 
    if not os.path.exists(Folder_Project_Descriptions_dir):
        os.makedirs(Folder_Project_Descriptions_dir)

    with open(File_Project_Descriptions_dir, "w") as prj_desc_file:
        prj_desc_file.write(summary)
