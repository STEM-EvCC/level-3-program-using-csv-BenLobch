import csv

# Give our in and out files some names
in_file = "security_incidents.csv"
out_file = "security_incidents_modified.csv"


# Read the CSV file 
with open(in_file, mode='r') as infile:
    reader = csv.reader(infile)
    incidents = list(reader)


# Make a new column and a default value
new_column_name = "Status"
default_value = 'Pending'


# Add the new column header
header = incidents[0] + [new_column_name]

# Add the new column value to each row
rows = [row + [default_value] for row in incidents[1:]]

# Write to new out CSV file 
with open(out_file, mode="w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Modified data saved to '{out_file}'")