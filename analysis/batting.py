def top_batsmen(df):
    top = df.groupby("batter")["batsman_runs"].sum() \
            .sort_values(ascending=False) \
            .head(10)
            
    print("/nTop 10 Batsmen ")
    print(top)
    
def strike_rate(df):
    # total runs
    runs = df.groupby("batter")["batsman_runs"].sum()
    
    # total balls faced
    balls = df.groupby("batter")["ball"].count()
    
    # strike rate 
    sr = (runs / balls) * 100
    
    # filter serious players 
    sr = sr[balls > 100]   # only players with 100+ balls
    
    print("\nTop Strick Rate ")
    print(sr.sort_values(ascending=False).head(10))
   
   # orange cap  
def orange_cap(df):
    runs = df.groupby("batter")["batsman_runs"].sum()
    
    top_player = runs.idxmax()
    top_runs = runs.max()
    
    print("\n orange cap winner")
    print(f"{top_player} - {top_runs} runs")
    
    # season - wise orange cap 
    
def orange_cap_season(df):
    # group by season + batter
    runs = df.groupby(["season" , "batter"])["batsman_runs"].sum().reset_index()
    
    # find top scorer per season 
    top = runs.loc[runs.groupby("season")["batsman_runs"].idxmax()]
    
    print("\n Orange cap (season-wise)")
    print(top.sort_values("season"))
    
 # Most Consistent Batsman 
 
def most_consistent_batsman(df):
    # total runs 
    runs = df.groupby("batter")["batsman_runs"].sum()
    
    # number of matches played
    matches = df.groupby("batter")["match_id"].nunique()
    
    # average runs per match
    avg = runs / matches
    
    # filter serious player
    avg = avg[matches > 50]
    
    print("\n Most Consistent Batsmen (Avg Runs per Match)")
    print(avg.sort_values(ascending=False).head(10))    
