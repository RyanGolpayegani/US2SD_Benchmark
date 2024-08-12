import os
import re
import csv
from tqdm import tqdm

def count_objects_in_uml(file_content):
    # Regex to match object definitions in PlantUML sequence diagrams
    # object_pattern = r'^\s*(?:participant|actor|boundary|control|entity|database|collections|queue|participant.*?)\s*".*?"\s*as\s+.*\b'
    # object_pattern = r'^\s*(?:participant|actor|boundary|control|entity|database|collections|queue|participant.*?)\s*(?:"[^"]*"|\w+)\s*as\s+.*\b'
    # object_pattern = r'^\s*(?:participant|actor|boundary|control|entity|database|collections|queue|participant.*?)\s*(?:"[^"]*"|\w+)(?:\s*as\s+\w+)?\b'
    # object_pattern = r'^\s*(?:participant|actor|boundary|control|entity|database|collections|queue|participant.*?)\s*(?:"[^"]*"|\w+)(?:\s*as\s+\w+)?\b'
    object_pattern = r'^\s*(participant|actor|boundary|control|entity|database|collections|queue)\s*(?:"[^"]*"|\w+)\s+as\s+\w+\b'




    
    # Find all matching lines in the file
    objects = re.findall(object_pattern, file_content, re.MULTILINE)

    
    # Return the count of unique objects
    return len(objects)


def process_directory(directory_path, output_csv):
    # Prepare the output CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['File Name', 'Object Count'])

        # Iterate over all files in the directory
        for filename in tqdm(os.listdir(directory_path)):
            if filename.endswith('.puml'):  # Check if the file is a PlantUML file
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r') as file:
                    file_content = file.read()
                    
                    # Count the number of objects in the sequence diagram
                    object_count = count_objects_in_uml(file_content)
                    
                    # Write the result to the CSV file
                    csvwriter.writerow([filename, object_count])

    print(f"Processing complete. Results are saved in {output_csv}")

# Directory containing the PlantUML files
directory_path = 'SD/2024_07_23__12_45_49/PUML'

# Output CSV file
output_csv = 'Judeges/object_counts.csv'

# Run the script
process_directory(directory_path, output_csv)
