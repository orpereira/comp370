import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset with the provided headers
df = pd.read_csv('/home/ubuntu/comp370/data/nyc_311_rat.csv')

# Step 1: Ensure 'created_date' is in datetime format
df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')

# Step 2: Filter for complaints related to rodents (rats and mice)
df_rodents = df

# Step 3: Group by 'location_type' (type of building/property) and count occurrences
grouped_df = df_rodents.groupby('location_type').size().reset_index(name='count')

# Step 4: Sort by the number of complaints for better visualization
grouped_df = grouped_df.sort_values(by='count', ascending=False)

# Step 5: Create a bar plot to show the frequency of complaints by location type
plt.figure(figsize=(12, 6))
sns.barplot(x='location_type', y='count', data=grouped_df, palette='viridis')

# Add titles and labels
plt.title('Distribution of Rodent-Related Complaints by Location Type')
plt.xlabel('Location Type')
plt.ylabel('Number of Complaints')

# Rotate x-axis labels if necessary
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.tight_layout()
plt.savefig('task2_plot.png')
