from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import pandas as pd
import os
from tqdm import tqdm

# Load Pegasus model and tokenizer
pegasus_model = PegasusForConditionalGeneration.from_pretrained(
    'google/pegasus-cnn_dailymail'
    )
tokenizer = PegasusTokenizer.from_pretrained(
    'google/pegasus-cnn_dailymail'
    )

df = pd.read_csv("data/All_US.csv")

# Combine all values in 'col1' into a string with comma (,) separator
project_names = df['Project Name'].unique()

print(f"Generating description for all projects with Pegasus ...")

# for loop here
for project in tqdm(project_names):
    combined_string = df.loc[df['Project Name'] == project, 'User Story'].str.cat(sep=', ')
    # print(f"This the combined for {project}:\n", combined_string)

    # Use the model and tokenizer for summarization
    inputs = tokenizer(
        [combined_string],
        max_length=1024,
        return_tensors='pt',
        truncation=True
        )

    summary_ids = pegasus_model.generate(
        inputs['input_ids'],
        num_beams=4,
        min_length=30,
        max_length=100
        )

    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
        )
    
    # Create the destination folder if it doesn't exist
    Folder_Project_Descriptions_dir = "data/Project_Descriptions/Pegasus" 
    File_Project_Descriptions_dir = f"data/Project_Descriptions/Pegasus/{project}.txt" 
    if not os.path.exists(Folder_Project_Descriptions_dir):
        os.makedirs(Folder_Project_Descriptions_dir)

    with open(File_Project_Descriptions_dir, "w") as prj_desc_file:
        prj_desc_file.write(summary)


##################### Input Example ###################
# input_text = "The internet has become an integral part of \
#     our daily lives. From communication to entertainment,\
#     education to business, it has transformed the way\
#     we interact with the world. Social media\
#     platforms like Facebook, Twitter, and Instagram allow us\
#     to connect with friends and family, share our thoughts\
#     and experiences"
##################################################333