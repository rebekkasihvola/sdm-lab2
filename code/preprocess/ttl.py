import re

# Function to remove the '.0' from Author values
def remove_decimal_from_author(match):
    # Extract the numeric part and ensure it is an integer
    original_value = match.group(1)
    integer_value = str(int(original_value))  # Convert to int and back to string to remove any '.0'
    return f'lab2:Author{integer_value}'

# Read the TTL file with UTF-8 encoding
with open('C:\\Users\\Dima\\SDM_submission\\sdm-lab2\\code\\abox\\abox.ttl', 'r', encoding='utf-8') as file:
    ttl_content = file.read()

# Use a regular expression to find and replace the author values with '.0'
# This regex captures floating point numbers after 'lab2:Author'
updated_ttl_content = re.sub(r'lab2:Author(\d+)\.0', remove_decimal_from_author, ttl_content)

# Write the updated content back to the TTL file with UTF-8 encoding
with open('C:\\Users\\Dima\\SDM_submission\\sdm-lab2\\code\\abox\\abox_nozeros.ttl', 'w', encoding='utf-8') as file:
    file.write(updated_ttl_content)

print("Updated TTL file saved as 'abox_nozeros.ttl'")