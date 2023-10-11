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

print(sorted_airports)

sns.scatterplot(data=sorted_airports,
                x="MedianArrDelay",
                y="TotalSeats",
                # hue=flights["TaxiOut"],
                # height=8,
                # aspect=1,
                palette='coolwarm_r')
# plt.yscale('log')

sns.regplot(data=sorted_airports,
            x="MedianArrDelay",
            y="TotalSeats",
            scatter=False,
            color='blue')

# sns.catplot(x="MedianArrDelay",
#             y="Orig",
#             kind="scatter",
#             data=sorted_airports,
#             order=sorted_airports.index, #airports["TotalSeats"].sort_values(ascending=True).index, # flights['Origin'].value_counts().index
#             height=8,
#             aspect=1,
#             palette='coolwarm_r')

# plt.text(sorted_airports.loc["SPI", "MedianArrDelay"], sorted_airports.index.get_loc("SPI"), "Test")

for index, row in sorted_airports.iterrows():
    plt.text(row["MedianArrDelay"], row["TotalSeats"], index, fontsize=8, color='black')

plt.yticks(rotation=45)
plt.yticks(fontsize=10)
plt.show()