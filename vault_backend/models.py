class LegoSet:

  def __init__(self, pieces, name, theme, set_num, year, price, type):
    self.pieces = pieces
    self.name = name
    self.theme = theme
    self.set_num = set_num
    self.year = year
    self.price = price
    self.type = type

  

  def display(self):
    nameprint = self.name.replace("_", " ").title()
    themeprint = self.theme.replace("-", " ").title()
    set_numprint = f"#{self.set_num}"
    priceprint = f"${self.price}"
    width = 40
    display = [
        f"\n"
        f"\n"
        f"┌{'─' * width}┐",
        f"│ Set {set_numprint:<{width - len('Set #')}}│",
        f"│ {nameprint:<{width - 1}}│",
        f"├{'─' * width}┤",
        f"│ Theme   : {themeprint:<{width - len('Theme   : ') - 1}}│",
        f"│ Year    : {self.year:<{width - len('Year    : ') - 1}}│",
        f"│ Price   : {priceprint:<{width - len('Price   : $')}}│",
        f"│ Pieces  : {self.pieces:<{width - len('Pieces  : ') - 1}}│",
        f"└{'─' * width}┘"]
    return '\n'.join(display)
                                                    
    
    
  
class OwnedLegoSet(LegoSet):

    def __init__(self, pieces, name, theme, set_num, year, price, type, status):
      super().__init__(pieces, name, theme, set_num, year, price, type)
      self.built_status = status

    def update_built_status(self, new_status):
      self.built_status = new_status


    def display(self):
      nameprint = self.name.replace("_", " ").title()
      themeprint = self.theme.replace("-", " ").title()
      set_numprint = f"#{self.set_num}"
      priceprint = f"${self.price}"
      statusprint = self.built_status.replace("_", " ").title()
      width = 40
      display = [
          f"\n"
          f"\n"
          f"┌{'─' * width}┐",
          f"│ Set {set_numprint:<{width - len('Set #')}}│",
          f"│ {nameprint:<{width - 1}}│",
          f"├{'─' * width}┤",
          f"│ Theme   : {themeprint:<{width - len('Theme   : ') - 1}}│",
          f"│ Year    : {self.year:<{width - len('Year    : ') - 1}}│",
          f"│ Price   : {priceprint:<{width - len('Price   : $')}}│",
          f"│ Pieces  : {self.pieces:<{width - len('Pieces  : ') - 1}}│",
          f"│ Type    : {self.type:<{width - len('Type    : ') - 1}}│"
          f"│ Built Status  : {statusprint:<{width - len('Built Status  : ') - 1}}│",
          f"└{'─' * width}┘"]

      return '\n'.join(display)

      
  

  

class WantedLegoSet(LegoSet):

  def __init__(self, pieces, name, theme, set_num, year, price, type, priority):
    super().__init__(pieces, name, theme, set_num, year, price, type)
    self.priority = priority


  def update_priority(self, new_priority):
    self.priority = new_priority


  def display(self):
    nameprint = self.name.replace("_", " ").title()
    themeprint = self.theme.replace("-", " ").title()
    set_numprint = f"#{self.set_num}"
    priceprint = f"${self.price}"
    priorityprint = self.priority.replace("_", " ").title()
    width = 40
    display = [
      f"\n"
      f"\n"
      f"┌{'─' * width}┐",
      f"│ Set {set_numprint:<{width - len('Set #')}}│",
      f"│ {nameprint:<{width - 1}}│",
      f"├{'─' * width}┤",
      f"│ Theme   : {themeprint:<{width - len('Theme   : ') - 1}}│",
      f"│ Year    : {self.year:<{width - len('Year    : ') - 1}}│",
      f"│ Price   : {priceprint:<{width - len('Price   : $')}}│",
      f"│ Pieces  : {self.pieces:<{width - len('Pieces  : ') - 1}}│",
      f"│ Type    : {self.type:<{width - len('Type    : ') - 1}}│"
      f"│ Priority  : {priorityprint:<{width - len('Priority  : ') - 1}}│",
      f"└{'─' * width}┘"]

    return '\n'.join(display)


  
  '''
┌────────────────────────────────────────┐
│ Set #75192                             │
│ Millennium Falcon                      │
├────────────────────────────────────────┤
│ Theme   : Star Wars                    │
│ Year    : 2017                         │
│ Price   : $849.99                      │
│ Pieces  : 7541                         │
│ Status  : owned                        │
└────────────────────────────────────────┘
'''

  