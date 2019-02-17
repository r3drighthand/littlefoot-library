# Import necessary libraries & files
import csv
# Will need to import return_record class

# Store ReturnRecords in list
return_records = []

# Parse target CSV & transform rows into ReturnRecord objects
with open('return_record.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimeter=',')
  for row in csv_reader:
    return_records.append(ReturnRecord(row[0], row[1], row[2], row[3], row[4]))