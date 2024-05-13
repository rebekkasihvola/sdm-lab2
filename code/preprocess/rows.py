import csv

# Function to split rows based on type and write to separate CSV files
def split_rows(input_file, journal_file, workshop_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        journal_rows = []
        workshop_rows = []

        for row in reader:
            if row[2] == 'journal':
                journal_rows.append(row)
            else:
                workshop_rows.append(row)

    # Write journal rows to a new CSV file
    with open(journal_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_STRINGS)

        writer.writerows(journal_rows)

    # Write workshop/conference rows to a new CSV file
    with open(workshop_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_STRINGS)
        writer.writerows(workshop_rows)

# Input and output filenames
input_filename = './data/publishers_cities.csv'  # Replace 'data.csv' with your CSV filename
journal_filename = 'journals.csv'
workshop_filename = 'workshop_conference.csv'

# Process CSV and create new CSV files for journals and workshop/conference rows
split_rows(input_filename, journal_filename, workshop_filename)