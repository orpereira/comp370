import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset (after removing 'Unnamed' columns)
df = pd.read_csv('/home/ubuntu/comp370/data/nyc_311_noise.csv', low_memory = False)

# Step 1: Ensure that 'opened' is in datetime format and extract the month
df['opened'] = pd.to_datetime(df['opened'], errors='coerce')  # Convert to datetime, coerce errors
df['month'] = df['opened'].dt.month_name()  # Extract month name

# Step 2: Filter complaints that contain the word 'NOISE' (if not already filtered)
df_noise = df[df['complaint_type'].str.contains('NOISE', case=False, na=False)]

# Step 3: Group by month and complaint_type, and count occurrences
grouped_df = df_noise.groupby(['month', 'complaint_type']).size().reset_index(name='count')

# Step 4: Pivot the table to prepare for heatmap visualization
pivot_df = grouped_df.pivot_table(index='month', columns='complaint_type', values='count', aggfunc='sum', fill_value=0)

# Step 5: Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_df, annot=True, fmt="d", cmap="YlGnBu", cbar=True)

# Add titles and labels
plt.title('Monthly Distribution of Noise Complaints by Cause')
plt.xlabel('Noise Category')
plt.ylabel('Month')

# Display the heatmap
plt.xticks(rotation=45)
# plt.show()
plt.savefig('noise_heatmap.png')
