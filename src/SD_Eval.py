import os
import csv
from tqdm import tqdm


def parse_plantuml(text):
  """
  This function parses PlantUML code and calculates complexity and quality metrics.

  **Note:** This is a simplified implementation and might need adjustments for intricate diagrams.
  """
  lifelines = set()
  messages = []
  nesting_depth = 0
  current_depth = 0
  alt_blocks = 0  # Count of alt blocks (contributes to cyclomatic complexity)
  opt_blocks = 0  # Count of opt blocks (contributes to cyclomatic complexity)

  for line in text.splitlines():
    if line.startswith("participant"):
      lifelines.add(line.split()[1])
    elif "->" in line:
      sender, receiver, *_ = line.split()
      messages.append((sender, receiver))
    elif "alt" in line:
      nesting_depth = max(nesting_depth, current_depth)
      current_depth += 1
      alt_blocks += 1
    elif "end" in line and line.startswith("  "):  # Assuming proper indentation for end alt
      current_depth -= 1
    elif "opt" in line:
      nesting_depth = max(nesting_depth, current_depth)
      current_depth += 1
      opt_blocks += 1
    elif "end" in line and line.startswith("    "):  # Assuming proper indentation for end opt
      current_depth -= 1

  # Message Cyclomatic Complexity (simplified)
  cyclomatic_complexity = len(messages) + 2  # Messages + decision points (1 for start, 1 for end)
  cyclomatic_complexity += alt_blocks + opt_blocks  # Add alt/opt block counts

  # Cohesion (basic check for single functionality based on message count)
  cohesion = "High" if len(messages) <= 5 else "Medium/Low"

  # Coupling (basic check for message exchange between all participants)
  coupling = "High" if len(set(msg[0] for msg in messages)) == len(lifelines) else "Medium/Low"

  # Completeness (basic check for missing responses based on message direction)
  unanswered_messages = [msg[0] for msg in messages if not any(rev_msg[1] == msg[0] for rev_msg in messages)]
  completeness = "High" if not unanswered_messages else "Incomplete (missing responses)"

  # Clarity (heuristic check for comments and short messages)
  clarity = "High" if ("//" in text and all(len(line.split()) <= 5 for line in messages)) else "Medium/Low"

  return {
      "lifelines": len(lifelines),
      "messages": len(messages),
      "nesting_depth": nesting_depth,
      "cyclomatic_complexity": cyclomatic_complexity,
      "cohesion": cohesion,
      "coupling": coupling,
      "completeness": completeness,
      "clarity": clarity
  }

parent_folder = "Experiment"
print(f"Evaluating all SDs in {parent_folder} folder ...")
for folder in tqdm(os.listdir(parent_folder)):
  source_dir = f"Experiment/{folder}/SDt"
  destination_dir = f"Experiment/{folder}/metrics.csv"
   


  with open(destination_dir, 'w', newline='') as output_file:
      # if the output file exists make it empty if it does not exist create an empty file
      csv_writer = csv.writer(output_file)
      csv_writer.writerow([
        'file name',
        'lifelines',
        'messages',
        'nesting_depth',
        'cyclomatic_complexity',
        'cohesion',
        'coupling',
        'completeness',
        'clarity',
        ])

      for file_name in os.listdir(source_dir):
          if file_name.endswith(".txt"):
              file_path = os.path.join(source_dir, file_name)
          with open(file_path, 'r') as file:
              plantuml_text = file.read()
          
          metrics = parse_plantuml(plantuml_text)

          my_list = [[
              str(file_name),
              metrics['lifelines'],
              metrics['messages'],
              metrics['nesting_depth'],
              metrics['cyclomatic_complexity'],
              metrics['cohesion'],
              metrics['coupling'],
              metrics['completeness'],
              metrics['clarity'],
              ]]
          # print(my_list)
          csv_writer = csv.writer(output_file)
          csv_writer.writerows(my_list)
              


          # print(f"Number of lifelines: {metrics['lifelines']}")
          # print(f"Number of messages: {metrics['messages']}")
          # print(f"nesting_depth: {metrics['nesting_depth']}")
          # print(f"cyclomatic_complexity: {metrics['cyclomatic_complexity']}")
          # print(f"cohesion: {metrics['cohesion']}")
          # print(f"coupling: {metrics['coupling']}")
          # print(f"completeness: {metrics['completeness']}")
          # print(f"clarity: {metrics['clarity']}")