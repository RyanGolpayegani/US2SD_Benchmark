import csv
from collections import Counter
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/All_US.csv")

sns.set_style("darkgrid")
sns.set_palette(["#FF5733", "#008080", "#800080"])

sns.catplot(
    y = 'Project Name',
    kind = 'count',
    data = df,
    height = 6,
    aspect = 1.5)
plt.title("Data Distribution ")
plt.xlabel("Number of User Stories")
plt.tight_layout()
plt.savefig("images/Data_Dist.png")
print("Figure saved in images/Data_Dist.png")
