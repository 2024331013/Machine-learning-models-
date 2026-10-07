import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd

# # df = pd.read_csv('social_media_dopamine_productivity.csv')
# # type_counts = df['nationality'].value_counts(ascending=True)

# # plt.barh(type_counts.index, type_counts.values, color= 'darkblue', edgecolor = 'black', linewidth = 0.5)
# # plt.title("Nationalities of students ")
# # plt.xlabel("Number of students")
# # plt.ylabel("Nationality", fontsize = 10 , color = "yellow")
# # plt.tight_layout()

# # plt.show()
# # print(type_counts)

# df = pd.read_csv('social_media_dopamine_productivity.csv')

# # for i , col in enumerate(df.columns[:10] ,start = 1 ):
# #     print(f"{i}: {col}")


# # print(df[["participant_id", "nationality", "age", "gender"]].head(10))

# filtered = df[(df["nationality"] == "Chinese") & (df["age"] > 15)]
# print(filtered)

help(pd.groupby)