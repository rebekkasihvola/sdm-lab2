import pandas as pd
import csv

# Read the first CSV file into a DataFrame
conferences_df = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/workshops.csv')

# Read the second CSV file into a DataFrame
editions_df = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/workshops_editions.csv')

# Merge the DataFrames based on the PublisherID, including all columns from the first CSV
merged_df = pd.merge(editions_df, conferences_df, on='PublisherID', how='left')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/Workshops_editions2.csv', index=False, quoting=csv.QUOTE_STRINGS)

print("Merged CSV file has been created as 'Workshops_editions2.csv'")
