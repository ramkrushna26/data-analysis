import pandas as pd

df = pd.read_csv("../../data/batting_summary.csv")

print("\nSort dataframe based on Match_no&Batting_Position: \n", 
	df.sort_values(by=["Match_no", "Batting_Position"], ascending=[False, True]).head())

print("\nDataframe column types: \n", df.dtypes)
 
print("\nTo get the list of all matches: \n", 
	df[["Match_no", "Match_Between"]].drop_duplicates().tail())

df["Rank"] = df["Match_no"].rank(ascending=False).astype(int)
print("\nAdd rank column based on existing column on dataframe: \n", 
	df[["Match_no", "Match_Between","Rank"]].drop_duplicates().head())

print("\nNo of matches played by each team: \n",
	df[["Match_no", "Team_Innings"]].drop_duplicates().Team_Innings.value_counts())

print("\nNo of matches played by each team: \n",
	df[["Match_no", "Team_Innings"]].drop_duplicates().groupby(["Team_Innings"], sort=True).count())

df_grp = df[["Match_no", "Team_Innings"]].drop_duplicates().groupby(["Team_Innings"])
print("\nGet the Match_no played by team India: \n", 
	df_grp.get_group("India"))
