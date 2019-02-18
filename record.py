class Record:
  def __init__(self, title, author, pages, decimal_category, read_status):
    self.title = title
    self.author = author
    self.pages = pages
    self.decimal_category = decimal_category
    self.read_status = read_status

  def get_dewey_decimal_category(self):
    # >>> string = str(12345.456)
    # >>> string
    # '12345.456'
    # >>> zero_index = string[0]
    # >>> zero_index
    # '1'

    if self.decimal_category == 000:
      return "Computer Science, Informtion, General Works"
    elif self.decimal_category == 100:
      return "Philosophy & Psychology"
    elif self.decimal_category == 200:
      return "Religion"
    elif self.decimal_category == 300:
      return "Social Sciences"
    elif self.decimal_category == 400:
      return "Language"
    elif self.decimal_category == 500:
      return "Pure Science"
    elif self.decimal_category == 600:
      return "Applied Science"
    elif self.decimal_category == 700:
      return "Arts & Recreation"
    elif self.decimal_category == 800:
      return "Literature"
    elif self.decimal_category == 900:
      return "Geography"
    else:
      return "Category Not Found!"

  # Sanity check:
  def get_title():
    print(self.title)

    
# PSEUDOCODE
# Grab first integer of DDC & assign variable
  # Need to convert decimal_category to string?
  # str.split() delimiter="."
    # "120.536DUC"
# Compare variable value with ddc
  # return correct category

