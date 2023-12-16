import pandas as pd

df = pd.read_csv("../../data/batting_summary.csv")

print("\nNo of records in dataframe: ", len(df.index))

# Squeeze will squeeze single row dataframe into Series
# Squeeze will squeeze series into scalars
dfs = pd.read_csv("../../data/batting_summary.csv", usecols=["Team_Innings"]).squeeze(axis=1)

def check_india(ind):
	if ind == "India":
		return True
	else:
		return False

print(dfs.apply(check_india).head())
