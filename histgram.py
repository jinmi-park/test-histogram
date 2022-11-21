import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv_file = './source_data.csv'

df = pd.read_csv(csv_file)

print(df)

sns.histplot(df['Result'])