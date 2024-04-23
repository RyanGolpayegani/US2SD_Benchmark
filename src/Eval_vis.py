import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

file_path = "../Experiment/metrics.csv"
df = pd.read_csv(file_path)

Counter(df['cohesion'])

sns.catplot(
    data = df,
    x = 'messages',
    y = 'folder name',
    hue = 'cohesion',
    kind = "violin",
    # bw=.15, cut=0,
    
)



sns.boxplot(
    data=df,
    y="folder name",
    x="messages",
)