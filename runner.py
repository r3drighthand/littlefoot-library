from return_record_parser import *
from record import *


def count_total_pages_read():
  total_pages = 0
  for record in return_records:
    pages_read = record.get_total_pages_read()
    total_pages += pages_read
  print("Total Pages Read: %s" %(total_pages))

def count_pages_by_category():
  category_dictionary = {}
  for record in return_records:
    key = record.get_decimal_category()
    value = record.get_total_pages_read()

    if key in category_dictionary:
      category_dictionary[key] += value
    else:
      category_dictionary[key] = value
  
  # Debugging
  print(category_dictionary)



# Formatting --
# Total Pages Read: number
# By Category: 
  # Philosophy: 333
  # Pure Science: 246
  # Computer Science: 90



count_total_pages_read()
count_pages_by_category()
