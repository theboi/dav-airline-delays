import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import sklearn

flights = pd.read_csv("./Flights.csv")
airports = pd.read_csv("./Airports.csv")

pd.set_option('display.max_columns', None)
print(flights.shape)
print(flights.loc[:, "ArrDelay"].describe(include="all"))


# print(flights.head(10))

# sns.catplot(x="ArrDelay",
#             y="Origin",
#             kind="strip",
#             data=flights,
#             order=flights['Origin'].value_counts().index,
#             height=9,
#             aspect=1,
#             palette='coolwarm_r')

# plt.show()
