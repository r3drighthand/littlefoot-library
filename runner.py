from return_record_parser import return_records, errors

def run_everything():
  print_errors()
  count_total_pages_read()
  count_pages_by_category()

def get_category_dictionary():
  category_dictionary = {}
  for record in return_records:
    key = record.get_decimal_category()
    value = record.get_total_pages_read()
    if key in category_dictionary:
      category_dictionary[key] += value 
    else:
      if value > 0:
        category_dictionary[key] = value
  return category_dictionary

def count_total_pages_read(): 
  dictionary = get_category_dictionary()
  total_pages = 0
  for key in dictionary:
    total_pages += dictionary[key]
  print "Total Pages Read: %s" %(total_pages)

def count_pages_by_category(): 
  dictionary = get_category_dictionary()
  print "By Category:"
  print '  ' + '  '.join(['{0}: {1}\n'.format(key, value) for key, value in dictionary.iteritems()])

def print_errors():
  if errors == 1:
    print "1 error \n" %(errors)
  elif errors > 1:
    print "%s errors \n" %(errors)
  else:
    print "0 errors \n"

####

run_everything()
