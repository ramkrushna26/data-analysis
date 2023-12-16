import pandas as pd
import numpy as np
import re

df = pd.read_csv("../../data/batting_summary.csv")

# Handling non-numeric cases
df["Strike_Rate"] = pd.to_numeric(df["Strike_Rate"].str.replace('-', ''), errors="coerce").fillna(0.00).astype(float)
df["Strike_Rate"] = df["Strike_Rate"].astype(float)

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

df_4s = df[["Batsman_Name","4s"]].groupby(["Batsman_Name"]).sum()
df_6s = df[["Batsman_Name","6s"]].groupby(["Batsman_Name"]).sum()
print("\nNo of 4s&6s hit by Batsman_Name: \n", 
	pd.concat([df_4s, df_6s], axis=1).sort_values(by=["4s","6s"], ascending=[False,False]))

df_sr = df[["Batsman_Name","Strike_Rate"]].groupby(["Batsman_Name"]).mean(numeric_only=True)
print("\nStrike rate by Batsman_Name: \n", 
	df_sr.sort_values(by=["Strike_Rate"], ascending=[False]).head())
