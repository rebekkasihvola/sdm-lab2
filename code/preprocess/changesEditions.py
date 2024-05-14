import csv

# Define file paths
editions_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/editions.csv"
conferences_editions_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/conferences_editions.csv"

# Create a set to store conference edition IDs
conference_edition_ids = set()

# Open conferences_editions.csv to extract conference edition IDs
with open(conferences_editions_file_path, "r", newline="") as conferences_editions_file:
    reader = csv.reader(conferences_editions_file)
    next(reader)  # Skip header
    for row in reader:
        conference_edition_ids.add(row[1])  # Assuming editionID is in the second column

# Open editions.csv to separate data
with open(editions_file_path, "r", newline="") as editions_file, \
     open("/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/workshops_editions_data.csv", "w", newline="") as workshop_output_file, \
     open("/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/conferences_editions_data.csv", "w", newline="") as conference_output_file:

    workshop_writer = csv.writer(workshop_output_file, quoting=csv.QUOTE_STRINGS)
    conference_writer = csv.writer(conference_output_file, quoting=csv.QUOTE_STRINGS)

    # Write headers to output files
    workshop_writer.writerow(["EditionID", "Type", "Date"])
    conference_writer.writerow(["EditionID", "Type", "Date"])

    reader = csv.reader(editions_file)
    for row in reader:
        edition_id = row[0]  # Assuming EditionID is in the first column
        if edition_id in conference_edition_ids:
            conference_writer.writerow(row)
        else:
            workshop_writer.writerow(row)

print("Data has been separated into workshops.csv and conferences.csv.")