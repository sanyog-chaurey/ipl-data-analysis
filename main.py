import pandas as pd 
from analysis import batting , bowling , team

# load data
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

# Merge
df = deliveries.merge(matches, left_on="match_id",right_on="id")
print("Data Loaded Successfully ")

# Analysis

# Batting
batting.top_batsmen(df)
batting.strike_rate(df)

# Bowling
bowling.top_bowlers(df)
bowling.economy_rate(df)

# Team
team.team_runs(df)

# orange cap
batting.orange_cap(df)

# puple cap
bowling.purple_cap(df)

# season wise orange cap 
batting.orange_cap_season(df)

# season wise purple cap
bowling.purple_cap_season(df)

from analysis import visualization

visualization.orange_cap_plot(df)
visualization.purple_cap_plot(df)

# successful team
team.most_successful_team(matches)

from analysis import visualization

visualization.top_batsmen_bar(df)

# Most Consistent Batsman 
batting.most_consistent_batsman(df)

from analysis import visualization
visualization.consistent_batsman_bar(df)