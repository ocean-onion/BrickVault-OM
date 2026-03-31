from ooomutils import colourprint, clear, wait, color


# Base class for all LEGO sets - holds shared attributes and display logic
class LegoSet:
    def __init__(self, pieces, name, theme, set_num, year, price, type):
        self.pieces = pieces
        self.name = name
        self.theme = theme
        self.set_num = set_num
        self.year = year
        self.price = price
        self.type = type  # "owned" or "wanted"

    # Overridden by child classes to add extra display rows
    def extra_lines_display(self, width):
        return []

    def display(self):
        # Format fields for display
        nameprint = self.name.replace("_", " ").title()
        themeprint = self.theme.replace("-", " ").title()
        set_numprint = f"#{self.set_num}"
        priceprint = f"${self.price}"

        width = 40

        # Build the ASCII box row by row
        display = [
            f"\n\n{color.CYAN}┌{'─' * width}┐",
            f"{color.CYAN}│{color.END}{color.YELLOW} Set {set_numprint:<{width - len('Set #')}}{color.END}{color.CYAN}│{color.END}",
            f"{color.CYAN}│{color.END} {nameprint:<{width - 1}}│",
            f"{color.CYAN}├{'─' * width}┤{color.END}",
            f"{color.CYAN}│{color.END} Theme   : {themeprint:<{width - len('Theme   : ') - 1}}│",
            f"{color.CYAN}│{color.END} Year    : {self.year:<{width - len('Year    : ') - 1}}│",
            f"{color.CYAN}│{color.END} Price   : {priceprint:<{width - len('Price   : $')}}│",
            f"{color.CYAN}│{color.END} Pieces  : {self.pieces:<{width - len('Pieces  : ') - 1}}│",
            f"{color.CYAN}│{color.END} Type    : {self.type:<{width - len('Type    : ') - 1}}│",
        ]

        # Append any child-class-specific rows (e.g. built status, priority)
        display.extend(self.extra_lines_display(width))
        display.append(f"└{'─' * width}┘")

        return f"{color.CYAN}" + f"\n{color.CYAN}".join(display) + f"{color.END}"


# Child class for sets the user owns - adds built status
class OwnedLegoSet(LegoSet):
    def __init__(self, pieces, name, theme, set_num, year, price, type, built_status):
        super().__init__(pieces, name, theme, set_num, year, price, type)
        self.built_status = built_status  # "built" or "unbuilt"

    def update_built_status(self, new_status):
        self.built_status = new_status

    # Adds the Built Status row to the display box
    def extra_lines_display(self, width):
        statusprint = self.built_status.replace("_", " ").title()
        return [
            f"│ Built Status  : {statusprint:<{width - len('Built Status  : ') - 1}}│"
        ]


# Child class for sets the user wants - adds priority
class WantedLegoSet(LegoSet):
    def __init__(self, pieces, name, theme, set_num, year, price, type, priority):
        super().__init__(pieces, name, theme, set_num, year, price, type)
        self.priority = priority  # "low", "medium", or "high"

    def update_priority(self, new_priority):
        self.priority = new_priority

    # Adds the Priority row to the display box
    def extra_lines_display(self, width):
        priorityprint = self.priority.replace("_", " ").title()
        return [f"│ Priority  : {priorityprint:<{width - len('Priority  : ') - 1}}│"]

    """
┌────────────────────────────────────────┐
│ Set #75192                             │
│ Millennium Falcon™                     │
├────────────────────────────────────────┤
│ Theme   : Star Wars™                   │
│ Year    : 2017                         │
│ Price   : $849.99                      │
│ Pieces  : 7541                         │
│ Status  : owned                        │
└────────────────────────────────────────┘
"""
