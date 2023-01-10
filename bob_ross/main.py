# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read csv file
df = pd.read_csv("dataset/elements-by-episode.csv")
print(df.head(3))

# amt_of_waterfalls = df["WATERFALL"].count()
# print(f"Waterfalls: {amt_of_waterfalls}")
# # Episodes by Season
# # parse EPISODE column strings, count(), plot()

# # Amount of Waterfalls

# # select columns by index
# print(df.iloc[:, [1, 2]])

# # select columns by range
# print(df.iloc[:, 2:])

# # select columns by name
# print(df.loc[:, ["CIRCLE_FRAME", "HALF_CIRCLE_FRAME"]])

# select columns by name as range
# print(df.loc[:, "FARM":"FLOWERS"])


def get_elements(painting):
    print("painting")
    title = painting.TITLE.replace('"', "")
    print(f"{painting.EPISODE}: {title}")

    for feature in painting[2:]:
        if feature.value >= 1:
            print(feature)

    elements = []
    return elements


# print("df.iloc[1]")
# print(df.iloc[1])
test = get_elements(df.iloc[1])

# print("test")
# print(test)
# get_elements(df[1])
