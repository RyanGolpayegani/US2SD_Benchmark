#%%
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
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

# %%
sns.set_theme(
    style='darkgrid',
    font_scale=1.2,
    # rc=custom_rcparams,
)


# Set style to ggplot
# plt.style.use('fivethirtyeight')
# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

fig = plt.figure(figsize=(9, 11))

plot = sns.catplot(
    data=df,
    x="folder name",
    y="messages",
    # hue='cohesion',
    kind='box',
    palette = 'pastel'
)
# palettes: ch:.25, Blues,
# plt.title("Number of Messages generated with each approach")
plt.ylabel("Messages")
plt.xlabel("Approach")
plt.xticks(rotation=90)

plt.savefig("../images/2.png", dpi=600, bbox_inches = 'tight')
# %%
