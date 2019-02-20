from return_record_parser import *

# Maybe change name to print_total_pages_read (more explicit)
def count_total_pages_read(): 
  total_pages = 0
  for record in return_records:
    pages_read = record.get_total_pages_read()
    total_pages += pages_read
  print "Total Pages Read: %s" %(total_pages)

# Maybe change name to print_pages_by_category (more explicit)
# Could refactor this into one method for both and delete count_total_pages_read because I'm calling record.get_total_pages_read() twice.
# Or could call count_total_pages_read() inside count_pages_by_category().
def count_pages_by_category(): 
  category_dictionary = {}
  for record in return_records:
    key = record.get_decimal_category()
    value = record.get_total_pages_read()

    if key in category_dictionary:
      category_dictionary[key] += value 
    else:
      if value > 0:
        category_dictionary[key] = value
  
  # Extract print and formatting statements into their own formatting method (separation of concerns)
  print "By Category:"
  print '  ' + '  '.join(['{0}: {1}\n'.format(k, v) for k,v in category_dictionary.iteritems()])


count_total_pages_read()
count_pages_by_category()
