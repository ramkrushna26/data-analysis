



df_zero = df["Runs"] == 0
df_balls = df["Balls"] > 0
print("\nGet all batsman who scored Zero: \n", 
	df[df_zero & df_balls][["Match_Between","Batsman_Name"]].head())

print("\nGet all batsman who scored between 150 or 200: \n", 
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
# print(df.pop("Strike_Rate"))
# print(df.head())

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

print("\nGet record of max runs scored by batsman: \n", 
	df.iloc[df["Runs"].idxmax()], df["Runs"].idxmax())

print("\nGet Teams in lower case: \n", 
	df["Team_Innings"].drop_duplicates().str.lower())

print("\ntimestamp of 2023-02-11: \n",
	pd.Timestamp("2023-02-11"))

#To convert string date field to datetime type 
#pd.to_datetime(df["date_column"])

print("\ntimestamp of 2023-02: \n",
	pd.Period("2023-02"))

print("\nStatistics of Rohit Sharma: \n", 
	df.loc[(df["Batsman_Name"] == "Rohit Sharma"), ["Batsman_Name", "Runs"]].describe())

print("\nStd of runs scored by Rohit Sharma: \n", 
	df.loc[(df["Batsman_Name"] == "Rohit Sharma"), ["Batsman_Name", "Runs"]].std(numeric_only=True))

print("\nMedian of runs scored by Rohit Sharma: \n", 
	df.loc[(df["Batsman_Name"] == "Rohit Sharma"), ["Batsman_Name", "Runs"]].median(numeric_only=True))


