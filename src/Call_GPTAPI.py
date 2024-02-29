import openai
import re
import csv
import pandas as pd
from datetime import datetime
import os

# Select first n US from csv
Number_of_SDs = 10
# Number_of_SDs += 1
Engine_model = "gpt-4"

# Specify the paths for the original and copy CSV files
original_filename = "data/All_US.csv"

# Set up the OpenAI API clientexplain the moon landing to a 6 years old in a few sentence
openai.api_key = input('Enter API key: ')

# Read USs and select N random US 
All_Data = pd.read_csv(original_filename)

# Make sure that it selects the same n random line in every run
random_seed = 123
N_Random_US = All_Data.iloc[1:].sample(n=Number_of_SDs, random_state=random_seed)

counter = 0
# Get the current time
current_time = datetime.now()
formatted_time = current_time.strftime("%Y_%m_%d__%H_%M_%S")
print("Formatted time:", formatted_time)

# Generate a response
for index, row in N_Random_US.iterrows():
    # Process each row here
    # print(f"Index: {index}")
    # print(row[4])
    # Access specific columns if needed
    # print(row['column_name'])
    counter += 1
    print(f"Generating SDt number {counter}...")

    # Create the prompt 
    user_story = row["User Story"]
    prompt = "This is my user story: " + user_story + " generate Sequence Diagram in Plant UML format"
    
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
    #print("This is GPT full answer:\n", gpt_full_answer)

    # Extract SDt code in PlantUML format
    # Define the regex pattern to match PlantUML code
    # This one is the old pattern which includes the word "plantUMl or UML in the actual code."
    # pattern = r'```(.+?)```'
    pattern = r'(@startuml.+?@enduml)'


    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, gpt_full_answer, re.DOTALL)
    #print(matches)
    for match in matches:
        #print("This is PlantUML code:")
        gpt_code_only = match.strip()
        #print(gpt_code_only)

    # Write the PlantUML code to txt file 
    # as ProjectName_NoOfLine.txt
    # And as Full_A_ProjectName_NoOfLine.txt
    

    text_file_name_code_only = f"SD/{formatted_time}/SDt/{row['Project Name']}_{row['No. of line']}.txt"
    dir_text_file_name_code_only = f"SD/{formatted_time}/SDt"

    text_file_name_full_answer = f"SD/{formatted_time}/Full_A_GPT/Full_A_{row['Project Name']}_{row['No. of line']}.txt"
    dir_text_file_name_full_answer = f"SD/{formatted_time}/Full_A_GPT"

    # Save PlantUML code
    # Create the directory if it doesn't exist
    if not os.path.exists(dir_text_file_name_code_only):
        os.makedirs(dir_text_file_name_code_only)
    with open(text_file_name_code_only, "w") as text_file_code_only:
        text_file_code_only.write(gpt_code_only)

    # Save GPT Full Answer
    if not os.path.exists(dir_text_file_name_full_answer):
        os.makedirs(dir_text_file_name_full_answer)
    with open(text_file_name_full_answer, "w") as text_file_full_answer:
        text_file_full_answer.write(gpt_full_answer)




##########################################################

# with open(original_filename, mode='r', newline='') as file:
#     reader_orig = csv.reader(file)
#     counter = 0

#     for row_orig in reader_orig:
#         counter += 1

#         # skip the first line which includes tags row
#         if counter == 1:
#             continue
#         # + 1 because the first line of the csv includes the tags
#         if counter == Number_of_SDs + 1:
#             break
#         user_story = row_orig[4]

#         print(f"Generating SDt {counter - 1}.")
#         # Prompt should be an string
#         prompt = "This is my user story:" + user_story + "generate Sequence Diagram in Plant UML format"

#         # Call gpt API
#         completion = openai.chat.completions.create(
#             model = Engine_model,
#             messages = [
#                 {
#                     "role" : "user",
#                     "content": prompt,
#                 }
#             ]
#         )

#         gpt_full_answer = completion.choices[0].message.content
#         #print("This is GPT full answer:\n", gpt_full_answer)

#         # Extract SDt code in PlantUML format
#         # Define the regex pattern to match PlantUML code
#         # This one is the old pattern which includes the word "plantUMl or UML in the actual code."
#         # pattern = r'```(.+?)```'
#         pattern = r'(@startuml.+?@enduml)'


#         # Find all matches of the pattern in the input string
#         matches = re.findall(pattern, gpt_full_answer, re.DOTALL)
#         #print(matches)
#         for match in matches:
#             #print("This is PlantUML code:")
#             gpt_code_only = match.strip()
#             #print(gpt_code_only)

#         # Write the PlantUML code to txt file 
#         # as ProjectName_NoOfLine.txt
#         # And as Full_A_ProjectName_NoOfLine.txt
#         text_file_name_code_only = f"SD/SDt/{row_orig[3]}_{row_orig[2]}.txt"
#         text_file_name_full_answer = f"SD/Full_A_GPT/Full_A_{row_orig[3]}_{row_orig[2]}.txt"

#         # Save PlantUML code
#         with open(text_file_name_code_only, "w") as text_file_code_only:
#             text_file_code_only.write(gpt_code_only)

#         # Save GPT Full Answer
#         with open(text_file_name_full_answer, "w") as text_file_full_answer:
#             text_file_full_answer.write(gpt_full_answer)
            
