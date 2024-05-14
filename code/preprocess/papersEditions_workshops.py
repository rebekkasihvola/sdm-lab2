import csv

# Define file paths
editions_papers_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/editions_papers.csv"
workshops_editions_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/workshops_editions.csv"

# Create a set to store workshop edition IDs
workshop_edition_ids = set()

# Open workshops_editions.csv to extract workshop edition IDs
with open(workshops_editions_file_path, "r", newline="") as workshops_editions_file:
    reader = csv.reader(workshops_editions_file)
    next(reader)  # Skip header
    for row in reader:
        workshop_edition_ids.add(row[1])  # Assuming editionID is in the second column

# Open editions_papers.csv to separate data
with open(editions_papers_file_path, "r", newline="") as editions_papers_file, \
     open("workshopEditions_papers.csv", "w", newline="") as workshop_output_file, \
     open("conferencesEditions_papers.csv", "w", newline="") as conference_output_file:

    workshop_writer = csv.writer(workshop_output_file, quoting=csv.QUOTE_STRINGS)
    conference_writer = csv.writer(conference_output_file, quoting=csv.QUOTE_STRINGS)

    # Write headers to output files
    workshop_writer.writerow(["EditionID", "paperID"])
    conference_writer.writerow(["EditionID", "paperID"])

    reader = csv.reader(editions_papers_file)
    next(reader)  # Skip header
    for row in reader:
        edition_id = row[0]  # Assuming EditionID is in the first column
        if edition_id in workshop_edition_ids:
            workshop_writer.writerow(row)
        else:
            conference_writer.writerow(row)

print("Data has been separated into workshopEditions_papers and conferencesEditions_papers.")
