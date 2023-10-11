import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import sklearn

flights = pd.read_csv("./data/flights.csv")
airports = pd.read_csv("./data/airports.csv", index_col="Orig")

pd.set_option('display.max_columns', None)
airports["MedianArrDelay"] = flights.groupby('Origin')['ArrDelay'].median()
airports.dropna(subset=['MedianArrDelay'], inplace=True)
sorted_airports = airports.sort_values(by='TotalSeats', ascending=False)
# sorted_airports = sorted_airports.head(30)

sns.catplot(x="MedianArrDelay",
            y="Orig",
            kind="strip",
            data=sorted_airports,
            order=sorted_airports.index, #airports["TotalSeats"].sort_values(ascending=True).index, # flights['Origin'].value_counts().index
            height=8,
            aspect=1,
            palette='coolwarm_r')

for code in ["SPI", "CMX", "JFK", "ATL"]:
    plt.text(sorted_airports.loc[code, "MedianArrDelay"], sorted_airports.index.get_loc(code), code)

# for index, row in sorted_airports.iterrows():
#     plt.text(row["MedianArrDelay"], row["TotalSeats"], index, fontsize=8, color='black')

plt.yticks(rotation=45)
plt.yticks(fontsize=10)
plt.show()