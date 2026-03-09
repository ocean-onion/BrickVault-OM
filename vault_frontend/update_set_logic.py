import os
from vault_backend.input_handlers.error_handler import NoSetsFoundError, Validator500000000
from vault_backend.vault_logic import VaultManager
from vault_backend.file_handler import update_split_files

class UpdateSetLogic:
    def __init__(self, vault_manager, set_num):
        self.vault_manager = vault_manager
        self.set_num = set_num

    def update_menu_owned(self):
        print("What would you like to update?")
        print("1. Name")
        print("2. Theme")
        print("3. Year")
        print("4. Price")
        print("5. Pieces")
        print("6. Built Status")
        print("7. Back to main menu")
        update_choice = Validator500000000.get_menu_choice(7)
        try:
            if update_choice == '1':
                new_name = Validator500000000.get_set_name("Enter the new name of the set: ")
                self.vault_manager.update_set_name(self.set_num, new_name)
                update_split_files(self.vault_manager)
                print("Lego set name updated successfully!")
    
            elif update_choice == '2':
                new_theme = Validator500000000.get_theme("Enter the new theme of the set: ")
                self.vault_manager.update_set_theme(self.set_num, new_theme)
                update_split_files(self.vault_manager)
                print("Lego set theme updated successfully!")
    
            elif update_choice == '3':
                new_year = Validator500000000.get_year("Enter the new year of the set: ")
                self.vault_manager.update_set_year(self.set_num, new_year)
                update_split_files(self.vault_manager)
                print("Lego set year updated successfully!")
    
            elif update_choice == '4':
                new_price = Validator500000000.get_price("Enter the new price of the set: ")
                self.vault_manager.update_set_price(self.set_num, new_price)
                update_split_files(self.vault_manager)
                print("Lego set price updated successfully!")
    
            elif update_choice == '5':
                new_piece_count = Validator500000000.get_pieces("Enter the new piece count of the set: ")
                self.vault_manager.update_set_pieces(self.set_num, new_piece_count)
                update_split_files(self.vault_manager)
                print("Lego set piece count updated successfully!")
    
            elif update_choice == '6':
                new_status = Validator500000000.get_status("Enter the new status of the set: ")
                self.vault_manager.update_set_status(self.set_num, new_status)
                update_split_files(self.vault_manager)
                print("Lego set status updated successfully!")

            elif update_choice == '7':
                return
            
        except NoSetsFoundError as e:
            print(e)

    def update_menu_wanted(self):
        print("What would you like to update?")
        print("1. Name")
        print("2. Theme")
        print("3. Year")
        print("4. Price")
        print("5. Pieces")
        print("6. Priority")
        print("7. Back to main menu")
        update_choice = Validator500000000.get_menu_choice(7)
        try:    
            if update_choice == '1':
                new_name = Validator500000000.get_set_name("Enter the new name of the set: ")
                self.vault_manager.update_set_name(self.set_num, new_name)
                update_split_files(self.vault_manager)
                print("Lego set name updated successfully!")

            elif update_choice == '2':
                new_theme = Validator500000000.get_theme("Enter the new theme of the set: ")
                self.vault_manager.update_set_theme(self.set_num, new_theme)
                update_split_files(self.vault_manager)
                print("Lego set theme updated successfully!")

            elif update_choice == '3':
                new_year = Validator500000000.get_year("Enter the new year of the set: ")
                self.vault_manager.update_set_year(self.set_num, new_year)
                update_split_files(self.vault_manager)
                print("Lego set year updated successfully!")

            elif update_choice == '4':
                new_price = Validator500000000.get_price("Enter the new price of the set: ")
                self.vault_manager.update_set_price(self.set_num, new_price)
                update_split_files(self.vault_manager)
                print("Lego set price updated successfully!")

            elif update_choice == '5':
                new_piece_count = Validator500000000.get_pieces("Enter the new piece count of the set: ")
                self.vault_manager.update_set_pieces(self.set_num, new_piece_count)
                update_split_files(self.vault_manager)
                print("Lego set piece count updated successfully!")

            elif update_choice == '6':
                new_priority = Validator500000000.get_priority("Enter the new priority of the set: ")
                self.vault_manager.update_set_priority(self.set_num, new_priority)
                update_split_files(self.vault_manager)
                print("Lego set status updated successfully!")

            elif update_choice == '7':
                return

        except NoSetsFoundError as e:
            print(e)
            

    def update_menu(self):
        for lego_set in self.vault_manager.set_list:
            if lego_set.set_num == self.set_num:
                if lego_set.type == "owned":
                    self.update_menu_owned()
                elif lego_set.type == "wanted":
                    self.update_menu_wanted()
                return