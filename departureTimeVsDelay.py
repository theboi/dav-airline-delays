import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import sklearn

flights = pd.read_csv("./data/flights.csv")
times = pd.DataFrame([f'{x}000'[:4] for x in range(24)])
print(times)

pd.set_option('display.max_columns', None)
# print(flights.shape)
# print(flights.loc[:, "ArrDelay"].describe(include="all"))

# print(flights.head(10))

# print(airports["TotalSeats"].sort_values(ascending=True).index)
flights['CRSDepTime'] = np.int32(np.ceil(flights['CRSDepTime']/100)*100)
print(flights['CRSDepTime'])
times["MedianArrDelay"] = flights.groupby('CRSDepTime')['ArrDelay'].median()
# airports.dropna(subset=['MedianArrDelay'], inplace=True)
# sorted_airports = airports.sort_values(by='TotalSeats', ascending=False)
# # sorted_airports = sorted_airports.head(51)

# print(sorted_airports)

# sns.catplot(x="MedianArrDelay",
#             y="Orig",
#             kind="strip",
#             data=sorted_airports,
#             order=sorted_airports.index, #airports["TotalSeats"].sort_values(ascending=True).index, # flights['Origin'].value_counts().index
#             height=8,
#             aspect=1,
#             palette='coolwarm_r')

# plt.yticks(rotation=45)
# plt.yticks(fontsize=10)
# plt.show()