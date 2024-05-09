import csv
import random

# List of smaller cities
cities = ["Austin", "Dublin", "Portland", "Brisbane", "Edinburgh", "Copenhagen", "Seville", "Krakow", "Valencia", "Helsinki", "New York", "London", "Tokyo", "Paris", "Los Angeles", "Berlin", "Sydney", "Toronto", "Rome", "Moscow"]

# Function to add city column for conference or workshop rows
def add_city_column(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]

    # Modify rows to add city column for conference or workshop rows
    modified_rows = []
    for row in rows:
        if row[2] == 'conference' or row[2] == 'workshop':
            city = random.choice(cities)
            row.append(city)
        modified_rows.append(row)

    # Write modified rows to a new CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_STRINGS)
        writer.writerows(modified_rows)

# Input and output filenames
input_filename = './data/publishers3.csv'  # Replace 'data.csv' with your CSV filename
output_filename = './data/modified_data.csv'

# Process CSV and create new CSV file with city column added
add_city_column(input_filename, output_filename)