import csv
from record import *

return_records = []
errors = 0

with open('return_record.csv') as csv_file:
  reader = csv.reader(csv_file, delimiter=',')
  next(reader)

  for row in reader:
    title = row[0]
    author = row[1]
    pages = row[2]
    decimal_category = row[3]
    read = row[4]

    try:
      pages_tested = int(pages)
    except:
      print "Did not find pages for: %s" %(title)
      errors += 1
      continue

    return_records.append(Record(title, author, pages, decimal_category, read))

# Need data validations before Record is created.
