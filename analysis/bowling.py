def top_bowlers(df) :
    wickets = df[df["is_wicket"] == 1]
    
    top = wickets["bowler"].value_counts().head(10)
    
    print("\nTop 10 Bowlers")
    print(top)
   
   # economy rate 
def economy_rate(df):
    # total runs given by bowler
    runs = df.groupby("bowler")["total_runs"].sum()
    
    # total balls bowled
    balls = df.groupby("bowler")["ball"].count()
    
    # convert ball -> overs
    overs = balls / 6
    
    economy = runs / overs
    
    # filters serious bowlers
    economy = economy[balls > 120] # at least 20 overs
    
    print("\nBest Economy ")
    print(economy.sort_values().head(10))
    
    # purple cap
def purple_cap(df):
    wickets = df[df["is_wicket"] == 1]
    
    bowler_wickets = wickets["bowler"].value_counts()
    
    top_bowler = bowler_wickets.idxmax()
    top_wickets = bowler_wickets.max()
    
    print("\n Purple Cap Winner")
    print(f"{top_bowler} - {top_wickets} wickets")
    
    # season-wise purple cap 
def purple_cap_season(df):
    # remove run-outs 
    wickets = df[
        (df["is_wicket"] == 1) &
        (df["dismissal_kind"] != "run out")
    ]
    
    # group by season + bowler 
    wkts = wickets.groupby(["season" , "bowler"]).size().reset_index(name="wickets")
    
    # find top bowler per season 
    top = wkts.loc[wkts.groupby("season")["wickets"].idxmax()]
    
    print("\n purple cap (season-wise)")
    print(top.sort_values("season"))