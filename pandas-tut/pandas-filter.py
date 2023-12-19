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

print("\nno of record in dataframe: \n", df.index)
df["Match_no"] = df["Match_no"].astype('category')
df.info()

df.set_index(keys="Match_no", inplace=True)
print(df.head())
df.reset_index(drop=False, inplace=True)
print(df.head())

print("\nIs 49 present in index: ", 49 in df.index)


print("\nGet index rows from 2 to 5: \n", df.loc[2:5])
print("\nGet index rows 50: \n", df.loc[50])


print("\nGet rows where batsman is Rohit and runs scored is >=100: \n", 
	df.loc[(df.Batsman_Name == "Rohit Sharma") & (df.Runs >= 100)])

print("\n50 index match: \n", 
	df.loc[50, "Match_Between"])

print("\nGet names of batsman who didn't face any balls: \n", 
	df.loc[(df.Balls == 0), ["Match_Between","Batsman_Name"]])


print("\nrename field runs as score: \n", 
	df.rename(mapper = {"Runs": "Score", "4s": "Fours", "6s": "Sixes"}, axis = 1).head())


print("\ndrop column strike_rate: \n", 
	df.drop(["Strike_Rate"], axis=1).head())

# Remove column from dataframe
#print(df.pop("Strike_Rate"))
#print(df.head())

print("\nSample: \n", df.sample())

print("\nSort values by Runs in desc: \n", 
	df.sort_values(by=["Runs"], ascending=False).head())

print("\nTop 5 most runs scored : \n", 
	df.nlargest(5, columns=["Runs"]))

print("\nTop 5 least runs scored by Rohit: \n", 
	df[df["Batsman_Name"] == "Rohit Sharma"].nsmallest(5, columns=["Runs"]))

print("\nColumns in dataframe: \n", df.columns)

print("\nBatsmans who hit more than 5 sixes: \n", 
	df.where(df["6s"] > 5).dropna().head())

print("\nRohit innings with more runs more than 50: \n", 
	df.query("Batsman_Name == 'Rohit Sharma' and Runs > 50"))


print("\nGet Teams: \n", df["Team_Innings"].unique())






