import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import sklearn

flights = pd.read_csv("./data/flights.csv")
airports = pd.read_csv("./data/airports.csv", index_col="Orig")

pd.set_option('display.max_columns', None)
airports["MaxArrDelay"] = flights.groupby('Origin')['ArrDelay'].max()
airports.dropna(subset=['MaxArrDelay'], inplace=True)
sorted_airports = airports.sort_values(by='TotalSeats', ascending=False)
# sorted_airports = sorted_airports.head(30)

sns.catplot(x="MaxArrDelay",
            y="Orig",
            kind="strip",
            data=sorted_airports,
            order=sorted_airports.index, #airports["TotalSeats"].sort_values(ascending=True).index, # flights['Origin'].value_counts().index
            height=8,
            aspect=1,
            palette='coolwarm_r')

for code in ["HNL", "CLT"]:
    plt.text(sorted_airports.loc[code, "MaxArrDelay"], sorted_airports.index.get_loc(code), f"{code}, {sorted_airports.loc[code, 'MaxArrDelay']}", ha='right')

# for index, row in sorted_airports.iterrows():
#     plt.text(row["MaxArrDelay"], row["TotalSeats"], index, fontsize=8, color='black')

plt.yticks(rotation=45)
plt.yticks(fontsize=10)
plt.show()