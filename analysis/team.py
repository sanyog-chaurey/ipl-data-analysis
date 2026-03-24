def team_runs(df):
    runs = df.groupby("batting_team")["total_runs"].sum() \
             .sort_values(ascending=False)
             
    print("\nTeam Total Runs ")
    print(runs)
    
def most_successful_team(matches):
    wins = matches["winner"].value_counts()
    
    print("\n Most successful Teams")
    print(wins.head(10))