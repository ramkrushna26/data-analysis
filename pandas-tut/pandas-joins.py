import pandas as pd

first_names = {
	"id" : [1, 2, 3, 7, 5],
	"first_name" : ["Virat", "Rohit", "Ravi", "Sachin", "Rahul"]
}

last_names = {
	"id" : [1, 3, 4, 5, 6],
	"last_name" : ["Kohli", "Jadeja", "Bumrah", "Dravid", "Iyyar"]
}

df_first = pd.DataFrame(first_names)
df_last = pd.DataFrame(last_names)

print("\nFirst Names DataFrame: \n", df_first.head())
print("\nLast Names DataFrame: \n", df_last.head())

print("\nInner Join: \n", pd.merge(df_first, df_last, on="id", how="inner"))
print("\nLeft Join: \n", pd.merge(df_first, df_last, on="id", how="left"))
print("\nRight Join: \n", pd.merge(df_first, df_last, on="id", how="right"))
print("\nOuter Join: \n", pd.merge(df_first, df_last, on="id", how="outer"))

print("\nIndex Join: \n", pd.merge(df_first, df_last, left_index=True, right_index=True))
