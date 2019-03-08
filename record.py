class Record:
  def __init__(self, title, author, pages, decimal_category, read): 
    self.title = str(title)
    self.author = str(author)
    self.pages = int(pages)
    self.decimal_category = str(decimal_category)
    self.read = str(read)

  def get_decimal_category(self):
    category_id = self.decimal_category[0]
    message_dictionary = {
      "0": "Computer Science", 
      "1": "Philosophy", 
      "2": "Religion", 
      "3": "Social Sciences", 
      "4": "Language", 
      "5": "Pure Science", 
      "6": "Applied Science", 
      "7": "Art", 
      "8": "Literature", 
      "9": "Geography"
    }
    for key in message_dictionary:
      try:
        if category_id == key:
          return message_dictionary[key]
      except:
        return "None" 
        # Need to change to work with error handling in Parser

  def get_total_pages_read(self):
    status = self.read
    message_dictionary = {
      "Fully": self.pages,
      "Partially": self.pages/2,
      "Unread": 0
    }
    for key in message_dictionary:
      if status == key:
        return message_dictionary[key]

