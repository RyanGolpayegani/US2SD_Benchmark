import os

def convert_txt_to_puml(directory):
    # Get all the files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            txt_filepath = os.path.join(directory, filename)
            puml_filepath = os.path.join(directory, filename.replace('.txt', '.puml'))
            
            # Read the content of the .txt file
            with open(txt_filepath, 'r') as txt_file:
                content = txt_file.read()
            
            # Write the content to a .puml file
            with open(puml_filepath, 'w') as puml_file:
                puml_file.write(content)
                    
    print("Conversion complete.")

# Usage
directory = 'SD/2024_07_23__12_45_49/PUML'  # Replace with the path to your directory
convert_txt_to_puml(directory)
