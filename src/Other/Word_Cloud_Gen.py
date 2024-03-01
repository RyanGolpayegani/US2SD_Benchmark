import csv
import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open("../data/All_US.csv", mode='r', newline='') as file:
    reader = csv.reader(file)
    mylist = []
    for row in reader:
        if row[4] == "User Story":
            continue
        mylist.append(row[4])





def generate_word_cloud(text_list):
    """
    Generate a word cloud from a list of strings.
    
    Args:
    text_list (list): List of strings.
    
    Returns:
    None. Displays the word cloud.
    """
    # Join all the strings in the list into a single string
    text = ' '.join(text_list)
    
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig("../images/Word_Cloud.png")
    plt.show()
    

# usage:
generate_word_cloud(mylist)
