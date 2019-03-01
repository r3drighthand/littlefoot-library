class Record:
  def __init__(self, title, author, pages, decimal_category, read): 
    self.title = title
    self.author = author
    self.pages = int(pages)
    self.decimal_category = str(decimal_category)
    self.read = str(read)

  def get_decimal_category(self):
    decimal_string = self.decimal_category
    category_indicator = decimal_string[0]

    if category_indicator == "0":
      return "Computer Science, Information, General Works"
    elif category_indicator == "1":
      return "Philosophy & Psychology"
    elif category_indicator == "2":
      return "Religion"
    elif category_indicator == "3":
      return "Social Sciences"
    elif category_indicator == "4":
      return "Language"
    elif category_indicator == "5":
      return "Pure Science"
    elif category_indicator == "6":
      return "Applied Science"
    elif category_indicator == "7":
      return "Arts & Recreation"
    elif category_indicator == "8":
      return "Literature"
    elif category_indicator == "9":
      return "Geography"
    else:
      return "X" # Need error handling here

  def get_total_pages_read(self):
    read_status = self.read
    if read_status == "Fully":
      return self.pages
    elif read_status == "Partially":
      return self.pages / 2
    elif read_status == "Unread":
      return 0
