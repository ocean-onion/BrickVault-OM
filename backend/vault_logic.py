from thefuzz import fuzz
class VaultManager:

  def __init__(self, set_list):
    self.set_list = set_list


  def add_set(self, new_set):
    self.set_list.append(new_set)

  def remove_set(self, set_num):
    for  i, lego_set in enumerate(self.set_list):
      if lego_set.set_num == set_num:
        self.set_list.pop(i)
        return True
      elif  i == len(self.set_list) - 1:
        return False
      else:
        continue

  # Get sets by name 

  def get_sets_by_name(self, name):
    return [lego_set for lego_set in self.set_list if name.lower() in lego_set.name.lower()]

  def get_sets_by_name_advanced(self, name):
    results = []
    for lego_sets in self.set_list:
      score = fuzz.token_set_ratio(name, lego_sets.name)
      if score > 70:
        results.append(lego_sets)
    return results
  
  # Get sets by one filter
  
  def get_sets_by_theme(self, theme):
    return [lego_set for lego_set in self.set_list if lego_set.theme == theme]

  def get_sets_by_year(self, year):
    return [lego_set for lego_set in self.set_list if lego_set.year == year]

  def get_sets_by_price_range(self, min_price, max_price):
    return [lego_set for lego_set in self.set_list if lego_set.price >= min_price and lego_set.price <= max_price]

  def get_sets_by_piece_count(self, min_pieces, max_pieces):
    return [lego_set for lego_set in self.set_list if lego_set.pieces >= min_pieces and lego_set.pieces <= max_pieces]

  def get_sets_by_status(self, status):
    return [lego_set for lego_set in self.set_list if lego_set.status == status]

  def get_all_sets(self):
    return self.set_list



  # Get set counts



  def get_set_count(self):
    return len(self.set_list)

  def get_set_count_by_theme(self, theme):
    return len([lego_set for lego_set in self.set_list if lego_set.theme == theme])

  def get_set_count_by_year(self, year):
    return len([lego_set for lego_set in self.set_list if lego_set.year == year])

  def get_set_count_by_price_range(self, min_price, max_price):
    return len([lego_set for lego_set in self.set_list if lego_set.price >= min_price and lego_set.price <= max_price])

  def get_set_count_by_piece_count(self, min_pieces, max_pieces):
    return len([lego_set for lego_set in self.set_list if lego_set.pieces >= min_pieces and lego_set.pieces <= max_pieces])

  def get_set_count_by_status(self, status):
    return len([lego_set for lego_set in self.set_list if lego_set.status == status])
  
  