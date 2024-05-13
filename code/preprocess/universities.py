import csv

# Define the file paths
affiliations_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/affiliations.csv"
university_affiliations_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/university_affiliations.csv"
company_affiliations_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/company_affiliations.csv"

# Open the affiliations.csv file and create output files for universities and companies
with open(affiliations_file_path, "r", newline="") as affiliations_file, \
        open(university_affiliations_file_path, "w", newline="") as university_affiliations_file, \
        open(company_affiliations_file_path, "w", newline="") as company_affiliations_file:
    reader = csv.reader(affiliations_file)
    university_writer = csv.writer(university_affiliations_file, quoting=csv.QUOTE_STRINGS)
    company_writer = csv.writer(company_affiliations_file, quoting=csv.QUOTE_STRINGS)
    
    # Write headers to output files
    university_writer.writerow(["AffiliationID", "AffiliationName", "Type"])
    company_writer.writerow(["AffiliationID", "AffiliationName", "Type"])
    
    # Iterate over each row in the affiliations.csv file
    for row in reader:
        # Determine the type of affiliation
        affiliation_type = row[2].strip()  # Get the type from the last column
        
        # Write the row to the appropriate output file
        if affiliation_type == "University":
            university_writer.writerow(row)
        elif affiliation_type == "Company":
            company_writer.writerow(row)