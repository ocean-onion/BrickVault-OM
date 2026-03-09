from ooomutils import clear, wait, colourprint_nl, color
def loading_screen():
  for i in range(1, 4):
      clear()
      colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Game{color.END}")
      wait(0.5)
      clear()
      colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Game.{color.END}")
      wait(0.5)
      clear()
      colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Game..{color.END}")
      wait(0.5)
      clear()
      colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Game...{color.END}")
      wait(0.5)
      clear()