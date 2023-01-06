# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read csv file
df = pd.read_csv("dataset/bob_ross_paintings.csv")
print(df.head(3))

print(
    f"""
Color Stats:

{df["num_colors"].describe()}
"""
)

# df["num_colors"].plot()
# plt.show(block=True)

print(df.groupby(["num_colors"])["num_colors"].count())

df.groupby(["num_colors"])["num_colors"].count().plot(
    kind="bar",
    title="Colors Used Frequency",
    xlabel="Colors Used (#)",
    ylabel="Occurences",
)

# df["num_colors"].plot(y=df.groupby("num_colors"))
plt.show(block=True)
