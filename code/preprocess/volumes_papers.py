import csv

# Read the volume ids from volumes.csv into a set
volume_ids = set()
with open('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/volumes.csv', newline='') as volumes_file:
    reader = csv.reader(volumes_file)
    for row in reader:
        volume_ids.add(row[0])

# Open editions_papers.csv and create two output files
with open('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/editions_papers_modified.csv', newline='') as input_file, \
        open('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/editions_papers_matched.csv', 'w', newline='') as matched_output_file, \
        open('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/editions_papers_unmatched.csv', 'w', newline='') as unmatched_output_file:

    reader = csv.reader(input_file)
    matched_writer = csv.writer(matched_output_file, quoting=csv.QUOTE_STRINGS)
    unmatched_writer = csv.writer(unmatched_output_file, quoting=csv.QUOTE_STRINGS)

    for row in reader:
        # Check if the second column of the row is in the set of volume ids
        if row[0] in volume_ids:
            matched_writer.writerow(row)
        else:
            unmatched_writer.writerow(row)
        

print("Processing completed.")