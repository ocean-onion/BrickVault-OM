from rich.color import Color
from ooomutils import colourprint, clear, wait, color


class LegoSet:
    def __init__(self, pieces, name, theme, set_num, year, price, type):
        self.pieces = pieces
        self.name = name
        self.theme = theme
        self.set_num = set_num
        self.year = year
        self.price = price
        self.type = type

    def extra_lines_display(self, width):
        return []

    def display(self):
        nameprint = self.name.replace("_", " ").title()
        themeprint = self.theme.replace("-", " ").title()
        set_numprint = f"#{self.set_num}"
        priceprint = f"${self.price}"

        width = 40
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

        display.extend(self.extra_lines_display(width))

        display.append(f"└{'─' * width}┘")

        return f"{color.CYAN}" + f"\n{color.CYAN}".join(display) + f"{color.END}"


class OwnedLegoSet(LegoSet):
    def __init__(self, pieces, name, theme, set_num, year, price, type, built_status):
        super().__init__(pieces, name, theme, set_num, year, price, type)
        self.built_status = built_status

    def update_built_status(self, new_status):
        self.built_status = new_status

    def extra_lines_display(self, width):
        statusprint = self.built_status.replace("_", " ").title()
        return [
            f"│ Built Status  : {statusprint:<{width - len('Built Status  : ') - 1}}│"
        ]


class WantedLegoSet(LegoSet):
    def __init__(self, pieces, name, theme, set_num, year, price, type, priority):
        super().__init__(pieces, name, theme, set_num, year, price, type)
        self.priority = priority

    def update_priority(self, new_priority):
        self.priority = new_priority

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
