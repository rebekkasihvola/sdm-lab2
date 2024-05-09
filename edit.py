import csv

# Function to split rows based on type and write to separate CSV files
def split_rows(input_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        edition_rows = []
        volume_rows = []

        for row in reader:
            if row[1] == 'edition':
                edition_rows.append(row)
            elif row[1] == 'volume':
                volume_rows.append(row)

    # Write edition rows to a new CSV file
    with open('edition.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_STRINGS)
        writer.writerows(edition_rows)

    # Write volume rows to a new CSV file
    with open('volume.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_STRINGS)
        writer.writerows(volume_rows)

# Input filename
input_filename = './data/editions.csv'  # Replace 'data.csv' with your CSV filename

# Process CSV and create new CSV files for edition and volume rows
split_rows(input_filename)