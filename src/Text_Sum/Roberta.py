from transformers import RobertaTokenizer, RobertaModel
import pandas as pd
import os
import torch
from tqdm import tqdm

# Load RoBERTa model and tokenizer
roberta_model = RobertaModel.from_pretrained('roberta-base')
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

df = pd.read_csv("data/All_US.csv")

# Combine all values in 'col1' into a string with comma (,) separator
project_names = df['Project Name'].unique()

print(f"Generating description for all projects with RoBERTa...")

# for loop here
for project in tqdm(project_names):
    combined_string = df.loc[df['Project Name'] == project, 'User Story'].str.cat(sep=', ')

    # Tokenize input text
    inputs = tokenizer.encode_plus(
        combined_string,
        add_special_tokens=True,
        return_tensors='pt',
        max_length=512,
        truncation=True
    )

    # Generate summary using RoBERTa
    with torch.no_grad():
        outputs = roberta_model(**inputs)
        summary_embeddings = outputs.last_hidden_state.mean(dim=1)  # Average pooling of hidden states
        summary_embeddings = summary_embeddings.unsqueeze(0)  # Add batch dimension

    # Decode summary embeddings
    summary_tokens = tokenizer.decode(summary_embeddings[0].argmax(dim=-1))

    # Create the destination folder if it doesn't exist
    Folder_Project_Descriptions_dir = "data/Project_Descriptions/RoBERTa" 
    File_Project_Descriptions_dir = f"data/Project_Descriptions/RoBERTa/{project}.txt" 
    if not os.path.exists(Folder_Project_Descriptions_dir):
        os.makedirs(Folder_Project_Descriptions_dir)

    with open(File_Project_Descriptions_dir, "w") as prj_desc_file:
        prj_desc_file.write(summary_tokens)
