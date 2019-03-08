import csv
import re
from record import *

return_records = []
# problem_records = []
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
      int(pages)
    except:
      print "Did not find pages for: %s" %(title)
      errors += 1
      continue

    try:
      pattern = re.compile("/^d{3}.d{3}w{3}/")
      pattern.match(decimal_category)
    except:
      print "Did not find Dewey Decimal Category for: %s" %(title)
      print "Error occured on line %s" %(reader.line_num)
      # problem_records.append(reader.line_num)
      errors += 1
      continue

    return_records.append(Record(title, author, pages, decimal_category, read))

# Need data validations before Record is created.
