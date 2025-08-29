# US2SD_Benchmark

This repositry includes all of the files associated with US2SD Benchmark which is a dataset of Sequence Diagrams (SD). These SDs are generated using ChatGPT.


## How to use:

<!-- 1. For using this tool first clone the this repo with following command:

```
git clone https://github.com/RezaGolpayegani/US2SD_Benchmark.git
``` -->

1. Go to the folder:

```
cd US2SD_Benchmark
```

2. Install the requirements:

```
pip install -r requirements
```

3. Now you should put your user stories in text files and put those text files in `data/All_US` folder, you must put the user stories which relate to same project in the same text file.

4. Run `src/US_to_CSV.py` finds all of the text files in `data/All_US` and creates `data/All_US.csv`. The first column of this csv file is the file number which referes number of the files that the script finds, second column is text file name, third column is line number in the corresponding text file, fourth column is project name which is extracted from text file names, and the content of the fifth column is user stories. You can run this script with the following command:

```
python src/US_to_CSV.py
```

6. Run `src/Call_GPTAPI.py` this script reads User Stories from the csv file which is created in the previous step and prompts them to ChatGPT 4 you can change the engine model in the script. The outputs of this script are the textual sequence diagram which are stored in `SD/SDT` folder and full answer of ChatGPT which is stored in `SD/Full_A_GPT`. You can run this script with the following command:

```
python src/Call_GPTAPI.py

```

7. Run `src/Call_PUML_API.py` this script sends the textual sequence diagrams to PlantUML Web Server [PlantUML Web Server](https://plantuml.com/sequence-diagram) using its API. The output of this script is visualized sequence diagrams in ".png" format which are stored in `SD/SDi` folder. You can run this script with the following command:

```
python src/Call_PUML_API.py

```

