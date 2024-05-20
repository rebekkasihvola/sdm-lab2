import pandas as pd
import csv

# Read the CSV file
df = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/reviews_papers.csv', header=None)

# Print the original data types
print("Original data types:\n", df.dtypes)

# Convert the second column (index 1) to string and ensure no floating point
df[1] = df[1].apply(lambda x: '{:.0f}'.format(x) if isinstance(x, float) else str(x))

# Print the modified data types
print("Modified data types:\n", df.dtypes)

# Save the modified DataFrame back to a CSV file if needed
df.to_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/modified_reviews_papers2.csv', index=False, header=False, quoting=csv.QUOTE_STRINGS)