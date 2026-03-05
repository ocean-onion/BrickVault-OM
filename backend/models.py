class Legoset:

  def __init__(self, pieces, name, theme, set_num, year, price):
    self.pieces = pieces
    self.name = name
    self.theme = theme
    self.set_num = set_num
    self.year = year
    self.price = price

  

  def __str__(self): 
    return f"{self.name} ({self.set_num}) - {self.pieces} pieces, {self.theme}, {self.year}, ${self.price}"

  
  def update_status(self, new_status):
    self.status = new_status
    