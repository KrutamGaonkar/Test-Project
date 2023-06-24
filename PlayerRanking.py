# Sample player data (replace with actual data)
player_data = [
    {"name": "SI", "runs": 1613, "average": 46.6 ,"centuries": 2},
    {"name": "VK", "runs": 12898, "average": 57.32, "centuries": 46},
    {"name": "SD", "runs": 6793, "average": 44.1, "centuries": 17},
    # Add more players...
]

# Step 1: Assign weights
weight_runs = 0.5
weight_average = 0.3
weight_centuries = 0.2

# Step 2: Normalize features
runs_values = [player["runs"] for player in player_data]
average_values = [player["average"] for player in player_data]
centuries_values = [player["centuries"] for player in player_data]

min_runs = min(runs_values)
max_runs = max(runs_values)
normalized_runs = [(player["runs"] - min_runs) / (max_runs - min_runs) for player in player_data]

min_avg = min(average_values)
max_avg = max(average_values)
normalized_avg = [(player["average"] - min_avg) / (max_avg - min_avg) for player in player_data]

min_centuries = min(centuries_values)
max_centuries = max(centuries_values)
normalized_centuries = [(player["centuries"] - min_centuries) / (max_centuries - min_centuries) for player in player_data]

# Step 3: Calculate combined scores
combined_scores = []
for i in range(len(player_data)):
    score = (
        normalized_runs[i] * weight_runs +
        normalized_avg[i] * weight_average +
        normalized_centuries[i] * weight_centuries
    )
    combined_scores.append(score)

# Step 4: Rank players based on combined scores
ranked_players = sorted(zip(player_data, combined_scores), key=lambda x: x[1], reverse=True)

# Print the ranking
for i, (player, score) in enumerate(ranked_players, start=1):
    print(f"Rank {i}: {player['name']} (Combined Score: {score})")
