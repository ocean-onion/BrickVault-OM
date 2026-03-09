from datetime import datetime

class ErrorName(Exception):
  logging = True
  
  def __init__(self, *args,):
    currenttime = datetime.now()
    class_name = self.__class__.__name__
    if ErrorName.logging:
      print(f"[{currenttime}] [LOG]: A {class_name} has occurred")
    super().__init__(*args)