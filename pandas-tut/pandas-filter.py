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

print("\nGet all innings by Rohit: \n", 
	df[df["Batsman_Name"] == "Rohit Sharma"])

print("\nGet all batsman who scored 100 or more: \n", 
	df[df["Runs"] >= 100][["Batsman_Name","Runs"]].head())

df_zero = df["Runs"] == 0
df_balls = df["Balls"] > 0
print("\nGet all batsman who scored Zero: \n", 
	df[df_zero & df_balls][["Match_Between","Batsman_Name"]].head())

print("\nGet all batsman who scored between 100 or 200: \n", 
	df[df["Runs"].between(150,200)][["Batsman_Name","Runs"]].head())

