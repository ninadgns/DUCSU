import pandas as pd

# Load the CSV
df = pd.read_csv('DUCSU Result - Updated.csv')

# Group by 'Post'
results = []
for post, group in df.groupby('Post'):
    # Find winner (Position == 1)
    winner = group[group['Position'] == 1].iloc[0]
    total_votes = group['Total'].sum()
    percent = (winner['Total'] / total_votes) * 100 if total_votes > 0 else 0
    results.append({
        'Post': post,
        'Winner': winner['Name'],
        'Winner Votes': winner['Total'],
        'Total Votes': total_votes,
        'Percentage': round(percent, 2)
    })

print("Post, Winner, Winner Votes, Total Votes, Percentage")
# Print results
for r in results:
    print(f"{r['Post']}, {r['Winner']}, {r['Winner Votes']} , {r['Total Votes']} , ({r['Percentage']}%)")