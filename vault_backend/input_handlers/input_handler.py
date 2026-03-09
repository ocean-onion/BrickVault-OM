from vault_backend.error_name_logic import ErrorName

# Custom Exceptions (For Input Handlers)


class FieldEmptyError(ErrorName):
  pass


class WordError(ErrorName):
  pass


class IntegerError(ErrorName):
  pass


class FloatError(ErrorName):
  pass


# Input Handlers


# Field Input (Checks if field is empty)
class FieldInput:

  @staticmethod
  def get(prompt):
    while True:
      value = input(prompt).strip()
      try:
        if not value:
          raise FieldEmptyError(
              f"You typed {value} which is empty. Please try again.")
        return value
      except FieldEmptyError as e:
        print(e)


class ValidateInput:

  @classmethod
  def get(cls, prompt):
    while True:
      value = FieldInput.get(prompt)
      try:
        return cls.validate(value)
      except ErrorName as e:
        print(e)

  @staticmethod
  def validate(value):
    raise NotImplementedError


# Word Input (Checks if field is a word)
class WordInput(ValidateInput):

  @staticmethod
  def validate(value):
      if not value.isalpha():
        raise WordError(
            f"You typed {value} which is not a word (Remove). Please try again."
        )
      return value


# Integer Input (Checks if field is an integer)
class IntegerInput(ValidateInput):

  @staticmethod
  def validate(value):
    if not value.isdigit():
      raise IntegerError(
          f"You typed {value} which is not an integer (0). Please try again.")
    return int(value)


# Float Input (Checks if field is a float)
class FloatInput(ValidateInput):

  @staticmethod
  def validate(value):
    if '.' not in value:
      raise FloatError(
          f"You typed '{value}' which is not a float (0.00). Please try again."
      )
    if not value.replace('.', '').isdigit():
      raise FloatError(
          f"You typed '{value}' which is not a float (0.00). Please try again."
      )
    return float(value)


# Validator (Combines all input handlers to be easily called in main)
class Validator2000:

  @staticmethod
  def get_word(prompt):
    return WordInput.get(prompt)

  @staticmethod
  def get_int(prompt):
    return IntegerInput.get(prompt)

  @staticmethod
  def get_float(prompt):
    return FloatInput.get(prompt)
