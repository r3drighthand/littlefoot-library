class Record:
  def __init__(self, title, author, pages, decimal_category, read):
    self.title = title
    self.author = author
    self.pages = pages
    self.decimal_category = decimal_category
    self.read = read
    # self.total_pages_read = None

  def get_decimal_category(self):
    decimal_string = str(self.decimal_category)
    category_indicator = decimal_string[0]

    if category_indicator == "0":
      return "Computer Science, Informtion, General Works"
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
    else:
      return "Geography"

  def get_total_pages_read(self):
    read_status = str(self.read)
    if read_status == "Fully":
      return int(self.pages)
    elif read_status == "Partially":
      return int(self.pages) / 2
    elif read_status == "Unread":
      return 0

