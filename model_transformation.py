import csv
import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the CSV file
df = pd.read_csv('users.csv')

# Identify duplicated IP addresses
duplicated_ips = df[df.duplicated('IP Address', keep=False)]

# Calculate the average post count
avg_post_count = df['Post Count'].mean()

# Identify users with high post counts
high_post_count_users = df[df['Post Count'] > avg_post_count * 2]

# Combine the two conditions
possible_bots = pd.concat([duplicated_ips, high_post_count_users]).drop_duplicates()

# Create an isolation forest model to identify anomalies
model = IsolationForest(contamination=0.1)
model.fit(possible_bots[['Post Count']])

# Predict anomalies (possible bots)
predictions = model.predict(possible_bots[['Post Count']])

# Identify possible bots
possible_bots['is_bot'] = predictions

# Print a list of possible bots
print("Possible Bots:")
print(possible_bots[possible_bots['is_bot'] == -1][['Username', 'First Name', 'Last Name']])

# Print a list of non-possible bots
print("\nNon-Possible Bots:")
print(possible_bots[possible_bots['is_bot'] == 1][['Username', 'First Name', 'Last Name']])

with open('possible_bots.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'First Name', 'Last Name', 'is_bot'])
    for index, row in possible_bots.iterrows():
        if row['is_bot'] == -1:
            writer.writerow([row['Username'], row['First Name'], row['Last Name'], row['is_bot']])

with open('non_possible_bots.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'First Name', 'Last Name', 'is_bot'])
    for index, row in possible_bots.iterrows():
        if row['is_bot'] == 1:
            writer.writerow([row['Username'], row['First Name'], row['Last Name'], row['is_bot']])
