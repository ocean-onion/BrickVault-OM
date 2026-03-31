from ooomutils import color,wait, clear
from vault_backend.input_handlers.error_handler import MenuError, MenuInput
from vault_backend.file_handler import load_from_json
from vault_backend.vault_logic import VaultManager

class MenuPage:
    def __init__(self, title, options):
        self.title = title
        self.options = options

class MenuDisplay:
    def __init__(self, vault_manager, pages):
        self.vault_manager = vault_manager
        self.pages = pages
        self.current_page = 0
        self.width = 40

    def display(self):
        page = self.pages[self.current_page]

        if self.current_page == 0:
            load_from_json(self.vault_manager, "jsons/owned_sets.json")
        elif self.current_page == 1:
            load_from_json(self.vault_manager, "jsons/wanted_sets.json")
        else:
            load_from_json(self.vault_manager, "jsons/sets.json")

        total = len(self.pages)

        wait(3)
        clear()

        print(f"\n{color.CYAN}┌{'─' * self.width}┐")

        print(
            f"{color.CYAN}│{color.END}"
            f"{color.YELLOW} {'BRICK SET VAULT':<{self.width-1}}"
            f"{color.END}{color.CYAN}│"
        )

        print(
            f"{color.CYAN}│{color.END}"
            f" {page.title:<{self.width-1}}"
            f"{color.CYAN}│"
        )

        print(
            f"{color.CYAN}│{color.END}"
            f" {'Page ' + str(self.current_page + 1) + ' of ' + str(total):<{self.width-1}}"
            f"{color.CYAN}│"
        )

        print(f"{color.CYAN}├{'─' * self.width}┤")

        for option in page.options:
            print(
                f"{color.CYAN}│{color.END}"
                f" {option:<{self.width-1}}"
                f"{color.CYAN}│"
            )

        print(f"{color.CYAN}├{'─' * self.width}┤")

        nav_options = [
            "N. Next page",
            "P. Prev page",
            "G. Go to page",
            "X. Exit",
        ]

        for nav in nav_options:
            print(
                f"{color.CYAN}│{color.END}"
                f" {nav:<{self.width-1}}"
                f"{color.CYAN}│"
            )

        print(f"{color.CYAN}└{'─' * self.width}┘{color.END}")
            

    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
        else:
            print("Already on last page.")

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print("Already on first page.")

    def go_to_page(self):
        page = input(f"Go to page (1-{len(self.pages)}): ").strip()
        if page.isdigit() and 1 <= int(page) <= len(self.pages):
            self.current_page = int(page) - 1
        else:
            print("Invalid page number.")

    def run(self):
        while True:
            self.display()
            choice = MenuInput.get(len(self.pages[self.current_page].options))
            if choice == 'n':
                self.next_page()
            elif choice == 'p':
                self.prev_page()
            elif choice == 'g':
                self.go_to_page()
            elif choice == 'x':
                return None
            else:
                return (self.current_page, choice)