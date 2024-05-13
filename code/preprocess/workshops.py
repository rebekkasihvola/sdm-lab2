import csv

# Open the original CSV file and create two new output files
with open('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/workshop_conference.csv', newline='') as input_file, \
        open('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/dataconferences.csv', 'w', newline='') as conferences_output_file, \
        open('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/dataworkshops.csv', 'w', newline='') as workshops_output_file:

    reader = csv.reader(input_file)
    conferences_writer = csv.writer(conferences_output_file, quoting=csv.QUOTE_STRINGS)
    workshops_writer = csv.writer(workshops_output_file, quoting=csv.QUOTE_STRINGS)

    for row in reader:
        # Check if the third column is "conference" or "workshop"
        if row[2] == "conference":
            conferences_writer.writerow(row)
        elif row[2] == "workshop":
            workshops_writer.writerow(row)

print("Processing completed.")