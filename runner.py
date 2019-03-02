from return_record_parser import return_records

def count_total_pages_read(): 
  total_pages = 0
  for record in return_records:
    pages_read = record.get_total_pages_read()
    total_pages += pages_read
  print "Total Pages Read: %s" %(total_pages)

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

  print "By Category:"
  print '  ' + '  '.join(['{0}: {1}\n'.format(k, v) for k, v in category_dictionary.iteritems()])

  # This iterates through the keys and values of the dictionary, creating a formatted string for each key/value pair.
  # There's a cleaner way to write this, without using join.
  # iteritems returns an iterator over the dictionary's (key, value) pairs.


  # Refactor count_pages_by_category and have it return the dictionary object
  # Then write methods that take that dictionary and apply logic to return (or print) the necessary data.




count_total_pages_read()
count_pages_by_category()
