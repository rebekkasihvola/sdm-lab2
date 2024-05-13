import csv

# Function to read publishers.csv and create a dictionary mapping publisher IDs to types
def create_publisher_type_dict(file_path):
    publisher_type_dict = {}
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            publisher_type_dict[row[0]] = row[2]  # Assuming the publisher ID is in the first column
    return publisher_type_dict

# Read publishers.csv to create the publisher type dictionary
publisher_type_dict = create_publisher_type_dict('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/publishers.csv')

# Open publishers_editions.csv and create output files for each type
with open('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/publishers_editions.csv', newline='') as input_file, \
        open('journals_editions.csv', 'w', newline='') as journals_output_file, \
        open('workshops_editions.csv', 'w', newline='') as workshops_output_file, \
        open('conferences_editions.csv', 'w', newline='') as conferences_output_file:

    reader = csv.reader(input_file)
    journals_writer = csv.writer(journals_output_file, quoting=csv.QUOTE_STRINGS)
    workshops_writer = csv.writer(workshops_output_file, quoting=csv.QUOTE_STRINGS)
    conferences_writer = csv.writer(conferences_output_file, quoting=csv.QUOTE_STRINGS)

    for row in reader:
        publisher_id = row[0]  # Assuming the publisher ID is in the first column
        # Check the type of the publisher using the dictionary
        publisher_type = publisher_type_dict.get(publisher_id)
        if publisher_type == "journal":
            journals_writer.writerow(row)
        elif publisher_type == "workshop":
            workshops_writer.writerow(row)
        elif publisher_type == "conference":
            conferences_writer.writerow(row)

print("Processing completed.")