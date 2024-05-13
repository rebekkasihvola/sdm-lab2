import csv

# Open editions_papers.csv and create a new output file
with open('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/editions_papers.csv', newline='') as input_file, \
        open('editions_papers_modified.csv', 'w', newline='') as output_file:

    reader = csv.reader(input_file)
    writer = csv.writer(output_file, quoting=csv.QUOTE_STRINGS)

    for row in reader:
        writer.writerow(row)

print("Processing completed.")