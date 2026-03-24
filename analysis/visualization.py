import matplotlib.pyplot as plt 

def orange_cap_plot(df):
    runs = df.groupby(["season" , "batter"])["batsman_runs"].sum().reset_index()
    top = runs.loc[runs.groupby("season")["batsman_runs"].idxmax()]
    
    plt.figure()
    plt.plot(top["season"], top["batsman_runs"], marker='o')
    
    for i in range(len(top)):
        plt.text(
            top["season"].iloc[i],
            top["batsman_runs"].iloc[i],
            top["batter"].iloc[i],
            fontsize=8
        )
        
    plt.title("Orange Cap Runs by Season")
    plt.xlabel("Season")
    plt.ylabel("Runs")
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    

def purple_cap_plot(df):
    wickets = df[
        (df["is_wicket"] == 1) &
        (df["dismissal_kind"] != "run out")
    ]
    
    wkts = wickets.groupby(["season", "bowler"]).size().reset_index(name="wickets")
    top = wkts.loc[wkts.groupby("season")["wickets"].idxmax()]
    
    plt.figure()
    plt.plot(top["season"], top["wickets"], marker='o')
    
    for i in range(len(top)):
        plt.text(
            top["season"].iloc[i],
            top["wickets"].iloc[i],
            top["bowler"].iloc[i],
            fontsize=8
        )
    
    plt.title("Purple Cap Wickets by Season")
    plt.xlabel("Season")
    plt.ylabel("Wickets")
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
def top_batsmen_bar(df):
    import matplotlib.pyplot as plt 
    
    top = df.groupby("batter")["batsman_runs"].sum() \
            .sort_values(ascending=False) \
            .head(10)
            
    plt.figure()
    plt.bar(top.index, top.values)
    
    plt.title("Top 10 Batsmen by Runs")
    plt.xlabel("Batsman")
    plt.ylabel("Runs")
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
def consistent_batsman_bar(df):
    import matplotlib.pyplot as plt
    
    runs = df.groupby("batter")["batsman_runs"].sum()
    matches = df.groupby("batter")["match_id"].nunique()
    
    avg = runs / matches
    avg = avg[matches > 50].sort_values(ascending=False).head(10)
    
    plt.figure()
    plt.bar(avg.index, avg.values)
    
    plt.title("Most Consistent Batsmen")
    plt.xlabel("player")
    plt.ylabel("Avg Runs per Match")
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()