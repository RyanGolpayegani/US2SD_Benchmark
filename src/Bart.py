from transformers import BartForConditionalGeneration, BartTokenizer
import pandas as pd
import os
from tqdm import tqdm

# Load BART model and tokenizer
bart_model = BartForConditionalGeneration.from_pretrained(
    'facebook/bart-large-cnn'
    )
tokenizer = BartTokenizer.from_pretrained(
    'facebook/bart-large-cnn'
    )

df = pd.read_csv("data/All_US.csv")

# Combine all values in 'col1' into a string with comma (,) separator
project_names = df['Project Name'].unique()

print(f"Generating description for all projects with BART...")

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

    summary_ids = bart_model.generate(
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
    Folder_Project_Descriptions_dir = "data/Project_Descriptions/BART" 
    File_Project_Descriptions_dir = f"data/Project_Descriptions/BART/{project}.txt" 
    if not os.path.exists(Folder_Project_Descriptions_dir):
        os.makedirs(Folder_Project_Descriptions_dir)

    with open(File_Project_Descriptions_dir, "w") as prj_desc_file:
        prj_desc_file.write(summary)
    
    # print("\n\n This is the Summarized text with BART:\n\n",
    #     summary,
    #     "\n\n\n")

################### Input Example #############################
# input_text = "\
#     The Industrial Revolution was a period of major\
#      technological advancement that took place during\
#      the late 18th and early 19th centuries, primarily in\
#      Europe and North America. It marked a significant shift\
#      from agrarian and handicraft-based economies to\
#      industrialized economies driven by machinery, factories,\
#           and mass production. \
#     \
#     The Industrial Revolution was characterized by several key\
#      innovations and developments across various industries.\
#      In the textile industry, the invention of the spinning\
#      jenny, spinning frame, and power loom revolutionized the\
#      production of textiles, leading to increased efficiency\
#      and output. In the transportation sector, the development\
#      of steam-powered locomotives and steamships revolutionized\
#      long-distance travel and trade, facilitating the movement\
#      of goods and people across vast distances.\
#     \
#     The Industrial Revolution also saw advancements in\
#      mining and metallurgy, with the widespread adoption of\
#      steam-powered pumps and engines for mining operations,\
#      as well as the introduction of new metallurgical\
#      processes such as the Bessemer process for steel\
#      production. These advancements fueled the growth of\
#      heavy industries such as iron and steel manufacturing,\
#      laying the foundation for modern infrastructure and\
#           construction.\
#     \
#     The impact of the Industrial Revolution was profound\
#      and far-reaching, transforming society, economy, and\
#      daily life in unprecedented ways. The shift from rural\
#      agrarian societies to urban industrial centers led to\
#      massive population growth in cities, accompanied by\
#      social and demographic changes. The rise of industrial\
#      capitalism and the emergence of factory-based production\
#      systems fundamentally altered labor relations and\
#      economic structures, giving rise to new social classes\
#      and dynamics.\
#     \
#     While the Industrial Revolution brought about\
#      unprecedented economic growth and technological\
#      progress, it also gave rise to significant social\
#      and environmental challenges. The rapid urbanization\
#      and industrialization led to overcrowded and unsanitary\
#      living conditions in urban areas, exacerbating issues\
#      of poverty, disease, and social inequality. The\
#      widespread use of fossil fuels and the expansion of\
#      industrial activities resulted in environmental\
#      degradation and pollution, contributing to long-term\
#      environmental challenges such as climate change and air\
#      and water pollution.\
#     \
#     Despite its challenges, the Industrial Revolution\
#      laid the groundwork for the modern world, shaping the\
#      trajectory of human history and setting the stage for\
#      further technological advancements and societal\
#      transformations in the centuries that followed."
#############################################################
