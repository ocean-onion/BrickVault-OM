import json
import os
from vault_backend.models import LegoSet, OwnedLegoSet, WantedLegoSet


# Saves all sets in the vault to a single JSON file
def save_to_json(vault_manager, filename):
    with open(filename, "w") as f:
        json.dump(
            [vars(lego_set) for lego_set in vault_manager.set_list],
            f,
            ensure_ascii=False,
            indent=4,
        )
        print(f"Lego sets changes saved to {filename}")
    return True


# Loads sets from a JSON file into the vault, creating the file if it doesn't exist
def load_from_json(vault_manager, filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist. Creating a new file.")
        with open(filename, "w") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return False

    if os.path.getsize(filename) == 0:
        print(f"File {filename} is empty. Creating a new file.")
        with open(filename, "w") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return False

    with open(filename, "r") as f:
        vault_manager.set_list = []
        setlist = json.load(f)

        # Reconstruct each set as the correct subclass based on its type field
        for legoset in setlist:
            if legoset["type"] == "owned":
                vault_manager.set_list.append(OwnedLegoSet(**legoset))
            elif legoset["type"] == "wanted":
                vault_manager.set_list.append(WantedLegoSet(**legoset))

    print(f"Lego sets loaded from {filename}")
    return True


# Writes owned and wanted sets to their respective split files, and updates the combined file
def update_split_files(vault_manager):
    owned_sets = []
    wanted_sets = []

    # Separate sets by type
    for lego_set in vault_manager.set_list:
        if lego_set.type == "owned":
            owned_sets.append(vars(lego_set))
        elif lego_set.type == "wanted":
            wanted_sets.append(vars(lego_set))

    total_sets = owned_sets + wanted_sets

    with open("jsons/owned_sets.json", "w") as f:
        json.dump(owned_sets, f, ensure_ascii=False, indent=4)

    with open("jsons/wanted_sets.json", "w") as f:
        json.dump(wanted_sets, f, ensure_ascii=False, indent=4)

    # Combined file used by search and count pages
    with open("jsons/sets.json", "w") as f:
        json.dump(total_sets, f, ensure_ascii=False, indent=4)

    print("Lego sets changes saved to jsons/owned_sets.json and jsons/wanted_sets.json")
    return True
