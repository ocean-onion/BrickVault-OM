from vault_backend.error_name_logic import ErrorName
from vault_backend.input_handlers.input_handler import ValidateInput, FieldInput
from datetime import datetime

  


class NoSetsFoundError(ErrorName):
  pass

class SetUpdateError(ErrorName):
  pass


class SetCreationError(ErrorName):
  pass


class SetNameError(ErrorName):
  pass


class ThemeError(ErrorName):
  pass


class YearError(ErrorName):
  pass


class BuiltStatusError(ErrorName):
  pass

class OwnedStatusError(ErrorName):
  pass

class PriorityStatusError(ErrorName):
  pass


class SetSearchError(ErrorName):
  pass


class SetNumberError(ErrorName):
  pass


class PriceError(ErrorName):
  pass


class PieceCountError(ErrorName):
  pass


class SetRemoveError(ErrorName):
  pass


class MenuError(ErrorName):
  pass


class SetNameInput(ValidateInput):

  @staticmethod
  def validate(value):
    set = value
    stripped_set = set
    ctr = [" ", "-", "_", ",", "+", "&", "™", "©", "®", "℗", "$", "%"]
    for cha in ctr:
      stripped_set = stripped_set.replace(cha, "")
    if not stripped_set.isalnum():
      raise SetNameError(f"You typed {set} which is not a name formatted correctly (Ferrari F2004 & Michael Schumacher). Please try again."
        )
    return set.lower().replace(" ", "_").replace(",", "_")


class ThemeInput(ValidateInput):

  @staticmethod
  def validate(value):
    theme = value
    stripped_theme = theme
    ctr = [" ", "-", "_", ",", "+", "&", "™", "©", "®", "℗", "$", "%"]
    for cha in ctr:
      stripped_theme = stripped_theme.replace(cha, "")
    if not stripped_theme.isalnum():
      raise ThemeError(f"You typed {theme} which is not a theme formatted correctly (Star Wars). Please try again."
        )
    return theme.lower().replace(" ", "-").replace(",", "-")


class YearInput(ValidateInput):

  @staticmethod
  def validate(value):
    year = value
    current_year = datetime.now().year
    if not year.isdigit():
        raise YearError(
            f"You typed {year} which is not a year formatted correctly (2023). Please try again."
        )
    if not 1949 <= int(year) <= current_year:
        raise YearError(
            f"You typed {year} which is not a valid year (1949-{current_year}). Please try again.")
    return int(year)


class BuiltStatusInput(ValidateInput):

  @staticmethod
  def validate(value):
    sta = value
    if not sta.replace(" ", "").isalpha():
      raise BuiltStatusError(
          f"You typed {sta} which is not a status formatted correctly (Built). Please try again."
      )
    return sta.lower().replace(" ", "")


class OwnedStatusInput(ValidateInput):
  
  @staticmethod
  def validate(value):
    sta = value
    if not sta.replace(" ", "").isalpha():
      raise OwnedStatusError(
          f"You typed {sta} which is not a status formatted correctly (Owned). Please try again."
      )
    return sta.lower().replace(" ", "")

class PriorityInput(ValidateInput):

  @staticmethod
  def validate(value):
    sta = value
    if not sta.replace(" ", "").isalpha():
      raise PriorityStatusError(
          f"You typed {sta} which is not a status formatted correctly (High). Please try again."
      )
    return sta.lower().replace(" ", "")


class SetSearchInput(ValidateInput):

  @staticmethod
  def validate(value):
    sfs = value

    if '.' in sfs:
      raise SetSearchError(
          f"You typed '{sfs}' which is not a valid set number or name. Please try again."
      )
    elif sfs.replace('-', '').isdigit():
      return int(sfs)
    else:
      return SetNameInput.validate(sfs)


class SetNumberInput(ValidateInput):

  @staticmethod
  def validate(value):
    sfs = value
    if not sfs.isdigit():
      raise SetNumberError(
          f"You typed {sfs} which is not a set number formatted correctly (12345). Please try again."
      )
    return int(sfs)


class PriceInput(ValidateInput):

  @staticmethod
  def validate(value):
    prc = value

    if '.' not in prc:
      raise PriceError(
          f"You typed '{prc}' which is not a price formatted correctly (0.00). Please try again."
      )
    return float(prc)


class PieceInput(ValidateInput):

  @staticmethod
  def validate(value):
      pic = value

      if not pic.isdigit():
        raise PieceCountError(
            f"You typed {pic} which is not a piece count formatted correctly (12345). Please try again."
        )
      return int(pic)


class MenuInput:
  @staticmethod
  def get(max_option):
      accepted = ["n", "p", "g", "x"]
      while True:
        value = FieldInput.get("Enter your choice: ")
        try:
          if value.lower() in accepted:
            return value.lower()
          elif value.isdigit():
            if int(value) < 1 or int(value) > max_option:
              raise MenuError(f"You typed {value} which is not a valid option (1-{max_option}). Please try again.")
            return value
          else:
            raise MenuError(f"You typed '{value}' which is not a valid option. Please try again.")
        except MenuError as e:
            print(e)


class Validator500000000:

  @staticmethod
  def get_set_name(prompt):
    return SetNameInput.get(prompt)

  @staticmethod
  def get_theme(prompt):
    return ThemeInput.get(prompt)

  @staticmethod
  def get_year(prompt):
    return YearInput.get(prompt)

  @staticmethod
  def get_status(prompt):
    return BuiltStatusInput.get(prompt)

  @staticmethod
  def get_set_search(prompt):
    return SetSearchInput.get(prompt)

  @staticmethod
  def get_set_number(prompt):
    return SetNumberInput.get(prompt)

  @staticmethod
  def get_price(prompt):
    return PriceInput.get(prompt)

  @staticmethod
  def get_pieces(prompt):
    return PieceInput.get(prompt)

  @staticmethod
  def get_menu_choice(max_option):
    return MenuInput.get(max_option)

  @staticmethod
  def get_owned_status(prompt):
    return OwnedStatusInput.get(prompt)

  @staticmethod
  def get_priority(prompt):
    return PriorityInput.get(prompt)
