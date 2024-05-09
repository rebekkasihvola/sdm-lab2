import csv

def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = [row for row in reader]

    # Modify last column to "workshop" if it is "unknown"
    modified_rows = []
    for row in rows:
        if row[-1] == "unknown":
            row[-1] = "workshop"
        modified_rows.append(row)

    # Write modified rows back to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_STRINGS)
        writer.writerows(modified_rows)

input_filename = './data/publishers.csv'  # Replace 'data.csv' with your CSV filename
output_filename = './data/modified_data3.csv'

# Process CSV and create new CSV file with last two columns modified
process_csv(input_filename, output_filename)