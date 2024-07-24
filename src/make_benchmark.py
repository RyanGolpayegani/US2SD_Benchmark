import openai
import re
import pandas as pd
from datetime import datetime
import os


# Engine_model = "gpt-4"
Engine_model = "gpt-4-0125-preview"

# Specify the paths for the original and copy CSV files
original_filename = "data/All_US.csv"

# Set up the OpenAI API clientexplain the moon landing to a 6 years old in a few sentence
openai.api_key = input('Enter API key: ')

# Read USs 
All_Data = pd.read_csv(original_filename)

# Get the current time
current_time = datetime.now()
formatted_time = current_time.strftime("%Y_%m_%d__%H_%M_%S")
print("Formatted time:", formatted_time)

# Loading prj desc
project_descriptions = {}
def read_project_descriptions(directory):
  """
  Reads project descriptions from a directory and stores them in a dictionary.

  Args:
      directory: The path to the directory containing project description files.

  Returns:
      A dictionary where keys are file names (without extension) and values are project descriptions (text content).
  """
  for filename in os.listdir(directory):
    # Ignore hidden files
    if filename.startswith('.'):
      continue
    # Get file path
    filepath = os.path.join(directory, filename)
    # Check if it's a regular file
    if os.path.isfile(filepath):
      # Extract filename without extension
      project_name = os.path.splitext(filename)[0]
      # Read file content
      with open(filepath, 'r') as file:
        description = file.read().strip()
      # Add to dictionary
      project_descriptions[project_name] = description

  return project_descriptions

project_dir = "data/Project_Descriptions/GPT4-Turbo"
descriptions = read_project_descriptions(project_dir)

counter = 0
# Generate a response
for index, row in All_Data.iterrows():
    counter += 1
    if counter <= 2012:
       continue
    print(f"Generating SDt number {counter}...")

    # Create the prompt 
    user_story = row["User Story"]
    project_name = row["Project Name"]
    prj_desc = descriptions[project_name]

    # Different Prompts 
    # Zero-Shot
    # prompt = "This is my user story: " + user_story + " generate detailed Sequence Diagram in Plant UML format"

    # DSP US + Prj desc
    prompt = "This is a project description:\n"\
    + prj_desc + "\nBased on this project description\
     generate detailed Sequence Diagram in Plant UML\
          format for this User Story:"\
          + user_story 

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

    # Extract SDt code in PlantUML format
    # Define the regex pattern to match PlantUML code
    # This one is the old pattern which includes the word "plantUMl or UML in the actual code."
    # pattern = r'```(.+?)```'
    pattern = r'(@startuml.+?@enduml)'


    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, gpt_full_answer, re.DOTALL)
    for match in matches:
        gpt_code_only = match.strip()

    # Write the PlantUML code to txt file as 0000_ProjectName_NoOfLine.txt and as 0000_Full_A_ProjectName_NoOfLine.txt
    text_file_name_code_only = f"SD/{formatted_time}/SDt/{counter:04d}_{row['Project Name']}_{row['No. of line']}.txt"
    dir_text_file_name_code_only = f"SD/{formatted_time}/SDt"

    text_file_name_full_answer = f"SD/{formatted_time}/Full_A_GPT/{counter:04d}_Full_A_{row['Project Name']}_{row['No. of line']}.txt"
    dir_text_file_name_full_answer = f"SD/{formatted_time}/Full_A_GPT"

    # Save PlantUML code & Create the directory if it doesn't exist
    if not os.path.exists(dir_text_file_name_code_only):
        os.makedirs(dir_text_file_name_code_only)
    with open(text_file_name_code_only, "w") as text_file_code_only:
        text_file_code_only.write(gpt_code_only)

    # Save GPT Full Answer
    if not os.path.exists(dir_text_file_name_full_answer):
        os.makedirs(dir_text_file_name_full_answer)  
    with open(text_file_name_full_answer, "w") as text_file_full_answer:
        text_file_full_answer.write(gpt_full_answer)
        