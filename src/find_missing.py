import os

# Specify the paths to your text and picture folders
text_folder = "Experiment/US BART/SDt"
picture_folder = "Experiment/US/SDi"
main_folder = "Experiment/US BART"

# Extract base filenames (without extensions) from the text files
text_filenames = [os.path.splitext(f)[0] for f in os.listdir(text_folder) if f.endswith(".txt")]

# Find missing files in the picture folder
missing_files = []
for filename in text_filenames:
   png_path = os.path.join(picture_folder, filename + ".png")
   if not os.path.exists(png_path):
       missing_files.append(filename + ".png")

# Print the names of the missing files
if missing_files:
   print("Missing files in the picture folder:")
   for missing_file in missing_files:
       print(missing_file)
else:
   print("No missing files found.")


with open(f"{main_folder}/missing.txt", 'w') as file:
   my_string = "\n".join(missing_files)
   file.write(my_string)
   