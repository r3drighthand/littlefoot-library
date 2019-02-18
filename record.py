class Record:
  def __init__(self, title, author, pages, decimal_number, read_status):
    self.title = title
    self.author = author
    self.pages = pages
    self.decimal_number = decimal_number
    self.read_status = read_status

  # Need to refactor long conditional logic
  def get_dewey_decimal_category(self, decimal_number):
    if self.decimal_number == 000:
      return "Computer Science, Informtion, General Works"
    elif self.decimal_number == 100:
      return "Philosophy & Psychology"
    elif self.decimal_number == 200:
      return "Religion"
    elif self.decimal_number == 300:
      return "Social Sciences"
    elif self.decimal_number == 400:
      return "Language"
    elif self.decimal_number == 500:
      return "Pure Science"
    elif self.decimal_number == 600:
      return "Applied Science"
    elif self.decimal_number == 700:
      return "Arts & Recreation"
    elif self.decimal_number == 800:
      return "Literature"
    elif self.decimal_number == 900:
      return "Geography"
    else:
      return "Category Not Found!"

    # print statements are working in REPL
