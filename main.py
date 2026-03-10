import ooomutils
from vault_backend.input_handlers.error_handler import MenuError, Validator500000000, NoSetsFoundError
from vault_backend.error_name_logic import ErrorName
from vault_backend.vault_logic import VaultManager
from vault_backend.models import OwnedLegoSet, WantedLegoSet
from vault_backend.file_handler import save_to_json, load_from_json, update_split_files
from vault_frontend.page_logic import MenuDisplay, MenuPage
from vault_frontend.update_set_logic import UpdateSetLogic

ooomutils.auto_update(printcheck=False, confirm=True, warn_on_breaking=True)
ErrorName.logging = True


def DoLoadingScreen():
    doloadingscreen = True
    name = "Lego Set Vault"
    if doloadingscreen:
        ooomutils.loading_screen(name)


def main():
    vault_manager = VaultManager([])
    DoLoadingScreen()
    ooomutils.wait(2)

    menu = MenuDisplay(vault_manager, [
        MenuPage("Manage Owned Sets", [
            "1. Add a Owned set", "2. Remove a Owned set",
            "3. Display all Owned sets", "4. Update a Owned set",
            "5. Change to Wanted set"
        ]),
        MenuPage("Manage Wanted Sets", [
            "1. Add a Wanted set",
            "2. Remove a Wanted set",
            "3. Display all Wanted sets",
            "4. Update a Wanted set",
            "5. Change to Owned set",
        ]),
        MenuPage("Search Sets", [
            "1. Search by name or number",
            "2. Search by theme",
            "3. Search by year",
            "4. Search by price range",
            "5. Search by piece count",
            "6. Search by built status",
            "7. Search by priority",
            "8. Search by type",
            "9. Display all sets",
        ]),
        MenuPage("Count Sets", [
            "1. Count all sets",
            "2. Count by theme",
            "3. Count by year",
            "4. Count by price range",
            "5. Count by piece count",
            "6. Count by built status",
            "7. Count by priority",
            "8. Count by type",
        ]),
    ])

    while True:
        result = menu.run()
        if not result:
            print("Exiting the Lego Set Vault. Goodbye!")
            break

        page, choice = result
        try:
            if page == 0:
                if choice == '1':
                    set_num = Validator500000000.get_set_number(
                        "Enter the set number: ")
                    name = Validator500000000.get_set_name(
                        "Enter the name of the set: ")
                    theme = Validator500000000.get_theme(
                        "Enter the theme of the set: ")
                    price = Validator500000000.get_price(
                        "Enter the price of the set: ")
                    year = Validator500000000.get_year(
                        "Enter the year of the set: ")
                    pieces = Validator500000000.get_pieces(
                        "Enter the number of pieces in the set: ")
                    status = Validator500000000.get_status(
                        "Enter the built status of the set: ")
                    lego_set = OwnedLegoSet(pieces, name, theme, set_num, year,
                                            price, "owned", status)
                    vault_manager.add_set(lego_set)
                    update_split_files(vault_manager)
                    print("Lego set added successfully!")

                elif choice == '2':
                    set_to_remove = Validator500000000.get_set_search(
                        "Enter the set number or name of the set to remove: ")
                    vault_manager.rm_set(set_to_remove)
                    update_split_files(vault_manager)
                    print("Lego set removed successfully!")

                elif choice == '3':
                    sets = vault_manager.get_sets()
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '4':
                    set_to_update = Validator500000000.get_set_number(
                        "Enter the set number of the set to update: ")
                    sets = vault_manager.get_sbnum(set_to_update)
                    for lego_set in sets:
                        print(lego_set.display())
                    UpdateSetLogic(vault_manager, set_to_update)

                elif choice == '5':
                    set_to_change = Validator500000000.get_set_number(
                        "Enter the set number of the set to change: ")
                    vault_manager.change_set_type(set_to_change)
                    update_split_files(vault_manager)

            elif page == 1:
                if choice == '1':
                    set_num = Validator500000000.get_set_number(
                        "Enter the set number: ")
                    name = Validator500000000.get_set_name(
                        "Enter the name of the set: ")
                    theme = Validator500000000.get_theme(
                        "Enter the theme of the set: ")
                    price = Validator500000000.get_price(
                        "Enter the price of the set: ")
                    year = Validator500000000.get_year(
                        "Enter the year of the set: ")
                    pieces = Validator500000000.get_pieces(
                        "Enter the number of pieces in the set: ")
                    priority = Validator500000000.get_priority(
                        "Enter the priority of the set: ")
                    lego_set = WantedLegoSet(pieces, name, theme, set_num,
                                             year, price, "wanted", priority)
                    vault_manager.add_set(lego_set)
                    update_split_files(vault_manager)
                    print("Lego set added successfully!")

                elif choice == '2':
                    set_to_remove = Validator500000000.get_set_search(
                        "Enter the set number or name of the set to remove: ")
                    vault_manager.rm_set(set_to_remove)
                    update_split_files(vault_manager)
                    print("Lego set removed successfully!")

                elif choice == '3':
                    sets = vault_manager.get_sets()
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '4':
                    set_to_update = Validator500000000.get_set_number(
                        "Enter the set number of the set to update: ")
                    sets = vault_manager.get_sbnum(set_to_update)
                    for lego_set in sets:
                        print(lego_set.display())
                    UpdateSetLogic(vault_manager, set_to_update)

                elif choice == '5':
                    set_to_change = Validator500000000.get_set_number(
                        "Enter the set number of the set to change: ")
                    vault_manager.change_set_type(set_to_change)
                    update_split_files(vault_manager)
                    print("Lego set changed successfully!")

            elif page == 2:
                if choice == '1':
                    sfs = Validator500000000.get_set_search(
                        "Enter the name or number of the set to search for: ")
                    sets = vault_manager.get_sbnum(sfs) if isinstance(
                        sfs, int) else vault_manager.get_sbn(sfs)
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '2':
                    theme = Validator500000000.get_theme(
                        "Enter the theme to search for: ")
                    sets = vault_manager.get_sbt(theme)
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '3':
                    year = Validator500000000.get_year(
                        "Enter the year to search for: ")
                    sets = vault_manager.get_sby(year)
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '4':
                    min_price = Validator500000000.get_price(
                        "Enter the minimum price: ")
                    max_price = Validator500000000.get_price(
                        "Enter the maximum price: ")
                    sets = vault_manager.get_sbpr(min_price, max_price)
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '5':
                    min_pieces = Validator500000000.get_pieces(
                        "Enter the minimum number of pieces: ")
                    max_pieces = Validator500000000.get_pieces(
                        "Enter the maximum number of pieces: ")
                    sets = vault_manager.get_sbpc(min_pieces, max_pieces)
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '6':
                    status = Validator500000000.get_status(
                        "Enter the status to search for: ")
                    sets = vault_manager.get_sbbst(status)
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '7':
                    priority = Validator500000000.get_priority(
                        "Enter the priority to search for: ")
                    sets = vault_manager.get_sbpt(priority)
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '8':
                    type = Validator500000000.get_owned_status(
                        "Enter the type to search for: ")
                    sets = vault_manager.get_sbty(type)
                    for lego_set in sets:
                        print(lego_set.display())

                elif choice == '9':
                    sets = vault_manager.get_sets()
                    for lego_set in sets:
                        print(lego_set.display())

            elif page == 3:
                if choice == '1':
                    print(
                        f"Total number of Lego sets: {vault_manager.get_sc()}")

                elif choice == '2':
                    theme = Validator500000000.get_theme(
                        "Enter the theme to count: ")
                    print(
                        f"Number of Lego sets with theme '{theme}': {vault_manager.get_scbt(theme)}"
                    )

                elif choice == '3':
                    year = Validator500000000.get_year(
                        "Enter the year to count: ")
                    print(
                        f"Number of Lego sets from year {year}: {vault_manager.get_scby(year)}"
                    )

                elif choice == '4':
                    min_price = Validator500000000.get_price(
                        "Enter the minimum price: ")
                    max_price = Validator500000000.get_price(
                        "Enter the maximum price: ")
                    print(
                        f"Number of Lego sets in price range ${min_price}-${max_price}: {vault_manager.get_scbpr(min_price, max_price)}"
                    )

                elif choice == '5':
                    min_pieces = Validator500000000.get_pieces(
                        "Enter the minimum number of pieces: ")
                    max_pieces = Validator500000000.get_pieces(
                        "Enter the maximum number of pieces: ")
                    print(
                        f"Number of Lego sets with piece count {min_pieces}-{max_pieces}: {vault_manager.get_scbpc(min_pieces, max_pieces)}"
                    )

                elif choice == '6':
                    status = Validator500000000.get_status(
                        "Enter the status to count: ")
                    print(
                        f"Number of Lego sets with status '{status}': {vault_manager.get_scbbst(status)}"
                    )

                elif choice == '7':
                    priority = Validator500000000.get_priority(
                        "Enter the priority to count: ")
                    print(
                        f"Number of Lego sets with priority '{priority}': {vault_manager.get_scpt(priority)}"
                    )

                elif choice == '8':
                    type = Validator500000000.get_owned_status(
                        "Enter the type to count: ")
                    print(
                        f"Number of Lego sets with type '{type}': {vault_manager.get_scty(type)}"
                    )

        except (NoSetsFoundError, MenuError) as e:
            print(e)
        input("\nPress Enter to continue...")
        ooomutils.clear()


main()
