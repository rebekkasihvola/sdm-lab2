import csv

input_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/authors_papers.csv"

# Open the input file
with open(input_file_path, "r", newline="") as input_file:
    # Create output files for main authors and coauthors
    with open("/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/datamain_authors.csv", "w", newline="") as main_file, \
         open("/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/datacoauthors.csv", "w", newline="") as coauthor_file:
        
        # Create CSV writers for output files
        main_writer = csv.writer(main_file, quoting=csv.QUOTE_STRINGS)
        coauthor_writer = csv.writer(coauthor_file, quoting=csv.QUOTE_STRINGS)
        
        # Write headers to output files
        main_writer.writerow(["AuthorID", "PaperID", "Type"])
        coauthor_writer.writerow(["AuthorID", "PaperID", "Type"])
        
        # Read input file and separate data
        reader = csv.reader(input_file)
        for row in reader:
            author_id, paper_id, author_type = row
            if author_type.strip().lower() == "main":
                main_writer.writerow([author_id, paper_id, author_type])
            elif author_type.strip().lower() == "coauthor":
                coauthor_writer.writerow([author_id, paper_id, author_type])

print("Data has been separated into main_authors.csv and coauthors.csv.")