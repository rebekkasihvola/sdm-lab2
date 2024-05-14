import csv
import uuid

# Define file paths
reviews_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/reviewers_papers.csv"
edited_reviews_file_path = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/edited_reviews.csv"

# Open the original reviews.csv file and create a new file for edited reviews
with open(reviews_file_path, "r", newline="") as reviews_file, \
     open(edited_reviews_file_path, "w", newline="") as edited_reviews_file:

    # Create CSV reader and writer objects
    reader = csv.reader(reviews_file)
    writer = csv.writer(edited_reviews_file, quoting=csv.QUOTE_STRINGS)

    # Write header to the new file
    writer.writerow(["reviewID", "AuthorID", "paperID", "content", "decision"])

    # Skip header in the original file
    next(reader)

    # Iterate over each row in the original file
    for row in reader:
        # Generate a random UUID for the reviewID column
        review_id = str(uuid.uuid4())

        # Append the reviewID to the row
        row_with_id = [review_id] + row

        # Write the row with reviewID to the new file
        writer.writerow(row_with_id)

print("Review IDs have been added to the data and saved to edited_reviews.csv.")