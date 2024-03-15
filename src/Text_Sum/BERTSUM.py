from transformers import BertTokenizer, BertModel
import pandas as pd
import os
from tqdm import tqdm
import torch

# Load BERT model and tokenizer
bert_model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

df = pd.read_csv("data/All_US.csv")

# Combine all values in 'col1' into a string with comma (,) separator
project_names = df['Project Name'].unique()

print(f"Generating description for all projects with BERTSUM...")

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

    # Generate summary using BERT
    with torch.no_grad():
        outputs = bert_model(**inputs)
        summary_embeddings = outputs.last_hidden_state.mean(dim=1)  # Average pooling of hidden states
        summary_embeddings = summary_embeddings.unsqueeze(0)  # Add batch dimension

    # Decode summary embeddings
    summary_tokens = tokenizer.decode(summary_embeddings[0].argmax(dim=-1))

    # Create the destination folder if it doesn't exist
    Folder_Project_Descriptions_dir = "data/Project_Descriptions/BERTSUM" 
    File_Project_Descriptions_dir = f"data/Project_Descriptions/BERTSUM/{project}.txt" 
    if not os.path.exists(Folder_Project_Descriptions_dir):
        os.makedirs(Folder_Project_Descriptions_dir)

    with open(File_Project_Descriptions_dir, "w") as prj_desc_file:
        prj_desc_file.write(summary_tokens)
