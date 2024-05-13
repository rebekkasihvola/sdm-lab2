import csv

# Define the file paths
affiliations_authors_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/affiliations_authors.csv"
affiliations_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/affiliations.csv"
university_affiliations_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/university_affiliations.csv"
company_affiliations_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/company_affiliations.csv"

# Read the affiliations.csv file to get the type of each affiliation
affiliation_types = {}
with open(affiliations_file_path, "r", newline="") as affiliations_file:
    reader = csv.reader(affiliations_file)

    for row in reader:
        affiliation_id, _, affiliation_type = row
        affiliation_types[affiliation_id] = affiliation_type

# Open the affiliations_authors file and create output files for universities and companies
with open(affiliations_authors_file_path, "r", newline="") as affiliations_authors_file, \
        open(university_affiliations_file_path, "w", newline="") as university_affiliations_file, \
        open(company_affiliations_file_path, "w", newline="") as company_affiliations_file:
    reader = csv.reader(affiliations_authors_file)
    university_writer = csv.writer(university_affiliations_file, quoting=csv.QUOTE_STRINGS)
    company_writer = csv.writer(company_affiliations_file, quoting=csv.QUOTE_STRINGS)
    
    # Write headers to output files
    university_writer.writerow(["AffiliationID", "AuthorID"])
    company_writer.writerow(["AffiliationID", "AuthorID"])
    
    # Iterate over each row in the affiliations_authors file
    for row in reader:
        affiliation_id, author_id = row
        
        # Check the type of the affiliation
        affiliation_type = affiliation_types.get(affiliation_id)
        if affiliation_type == "University":
            # Write the row to the university affiliations file
            university_writer.writerow([affiliation_id, author_id])
        elif affiliation_type == "Company":
            # Write the row to the company affiliations file
            company_writer.writerow([affiliation_id, author_id])