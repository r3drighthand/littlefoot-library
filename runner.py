from return_record_parser import *
from record import *


def count_total_pages_read():
  total_pages = 0
  for record in return_records:
    pages_read = record.get_total_pages_read()
    total_pages += pages_read
  print(total_pages)

# def count_pages_by_category():
  # loop thru records list
  # use dictionary to assign category as KEY and pages read for category as VALUE





count_total_pages_read()
