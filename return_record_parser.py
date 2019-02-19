import csv
from record import *

return_records = []

with open('return_record.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    return_records.append(Record(row[0], row[1], row[2], row[3], row[4]))
