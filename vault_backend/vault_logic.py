from thefuzz import fuzz
from vault_backend.models import LegoSet, OwnedLegoSet, WantedLegoSet
from vault_backend.input_handlers.error_handler import NoSetsFoundError
import json


class VaultManager:
    def __init__(self, set_list):
        self.set_list = set_list

    # Returns True if a set with the given number already exists
    def is_duplicate(self, set_num):
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                return True
        return False

    # Raises an error if a search returned no results
    def query_results_check(self, results, filter, input):
        if not results:
            raise NoSetsFoundError(
                f"There are no sets in the vault with {filter} {input}."
            )
        return results

    # Raises an error if a count returned zero
    def count_results_check(self, count, filter, input):
        if count == 0:
            raise NoSetsFoundError(
                f"There are no sets in the vault with {filter} {input}."
            )
        return count

    # Adds a set to the vault if no duplicate set number exists
    def add_set(self, new_set):
        if self.is_duplicate(new_set.set_num):
            print(f"Set {new_set.set_num} already exists in the vault.")
            return False
        else:
            self.set_list.append(new_set)
            return True

    # Removes a set by set number or name
    def rm_set(self, set_trm):
        for i, lego_set in enumerate(self.set_list):
            if lego_set.set_num == set_trm or lego_set.name == set_trm:
                self.set_list.pop(i)
                return True
        raise NoSetsFoundError(
            f"There are no sets in the vault with set number or name {set_trm}."
        )

    # --- Update methods ---

    def update_set_num(self, set_num, new_set_num):
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                lego_set.set_num = new_set_num
                return True
        raise NoSetsFoundError(
            f"There are no sets in the vault with set number {set_num}."
        )

    def update_set_name(self, set_num, new_name):
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                lego_set.name = new_name
                return True
        raise NoSetsFoundError(
            f"There are no sets in the vault with set number {set_num}."
        )

    def update_set_theme(self, set_num, new_theme):
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                lego_set.theme = new_theme
                return True
        raise NoSetsFoundError(
            f"There are no sets in the vault with set number {set_num}."
        )

    def update_set_year(self, set_num, new_year):
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                lego_set.year = new_year
                return True
        raise NoSetsFoundError(f"There are no sets in the vault with number {set_num}.")

    def update_set_status(self, set_num, new_status):
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                lego_set.update_built_status(new_status)
                return True
        raise NoSetsFoundError(f"There are no sets in the vault with number {set_num}.")

    def update_set_priority(self, set_num, new_priority):
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                lego_set.update_priority(new_priority)
                return True
        raise NoSetsFoundError(f"There are no sets in the vault with number {set_num}.")

    # Converts a set between owned and wanted by replacing it with the correct subclass
    def change_set_type(self, set_num):
        for i, lego_set in enumerate(self.set_list):
            if lego_set.set_num == set_num:
                if lego_set.type == "owned":
                    new_set = WantedLegoSet(
                        lego_set.pieces,
                        lego_set.name,
                        lego_set.theme,
                        lego_set.set_num,
                        lego_set.year,
                        lego_set.price,
                        "wanted",
                        "medium",
                    )
                elif lego_set.type == "wanted":
                    new_set = OwnedLegoSet(
                        lego_set.pieces,
                        lego_set.name,
                        lego_set.theme,
                        lego_set.set_num,
                        lego_set.year,
                        lego_set.price,
                        "owned",
                        "unbuilt",
                    )
                self.set_list[i] = new_set
                return True
        raise NoSetsFoundError(
            f"There are no sets in the vault with set number {set_num}."
        )

    def update_set_price(self, set_num, new_price):
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                lego_set.price = new_price
                return True
        raise NoSetsFoundError(f"There are no sets in the vault with number {set_num}.")

    def update_set_pieces(self, set_num, new_pieces):
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                lego_set.pieces = new_pieces
                return True
        raise NoSetsFoundError(f"There are no sets in the vault with number {set_num}.")

    # --- Search methods (return matching sets) ---

    # Fuzzy search by name
    def get_sbn(self, name):
        sbn_qr = []
        for lego_sets in self.set_list:
            sbn_qs = fuzz.token_set_ratio(name, lego_sets.name)
            if sbn_qs > 70:
                sbn_qr.append(lego_sets)
        return self.query_results_check(sbn_qr, "name", name)

    # Exact match by set number
    def get_sbnum(self, set_num):
        sbnum_qr = []
        for lego_set in self.set_list:
            if lego_set.set_num == set_num:
                sbnum_qr.append(lego_set)
        return self.query_results_check(sbnum_qr, "set number", set_num)

    # Fuzzy search by theme
    def get_sbt(self, theme):
        sbt_qr = []
        for lego_set in self.set_list:
            sbt_qs = fuzz.token_set_ratio(theme, lego_set.theme)
            if sbt_qs > 70:
                sbt_qr.append(lego_set)
        return self.query_results_check(sbt_qr, "theme", theme)

    def get_sby(self, year):
        result = [lego_set for lego_set in self.set_list if lego_set.year == year]
        return self.query_results_check(result, "year", year)

    def get_sbpr(self, min_price, max_price):
        result = [
            lego_set
            for lego_set in self.set_list
            if lego_set.price >= min_price and lego_set.price <= max_price
        ]
        return self.query_results_check(result, "price", f"{min_price} and {max_price}")

    def get_sbpc(self, min_pieces, max_pieces):
        result = [
            lego_set
            for lego_set in self.set_list
            if lego_set.pieces >= min_pieces and lego_set.pieces <= max_pieces
        ]
        return self.query_results_check(
            result, "piece count", f"{min_pieces} and {max_pieces}"
        )

    # hasattr guards against searching owned sets for priority (and vice versa)
    def get_sbbst(self, built_status):
        result = [
            lego_set
            for lego_set in self.set_list
            if hasattr(lego_set, "built_status")
            and lego_set.built_status == built_status
        ]
        return self.query_results_check(result, "built status", built_status)

    def get_sbpt(self, priority):
        result = [
            lego_set
            for lego_set in self.set_list
            if hasattr(lego_set, "priority") and lego_set.priority == priority
        ]
        return self.query_results_check(result, "priority", priority)

    def get_sbty(self, type):
        result = [lego_set for lego_set in self.set_list if lego_set.type == type]
        return self.query_results_check(result, "type", type)

    def get_sets(self):
        result = self.set_list
        return self.query_results_check(result, "sets", "all")

    # --- Count methods (return ithe number of sets in that with that attr) ---

    def get_sc(self):
        result = len(self.set_list)
        return self.count_results_check(result, "sets", "all")

    def get_scbt(self, theme):
        results = len(
            [lego_set for lego_set in self.set_list if lego_set.theme == theme]
        )
        return self.count_results_check(results, "theme", theme)

    def get_scby(self, year):
        result = len([lego_set for lego_set in self.set_list if lego_set.year == year])
        return self.count_results_check(result, "year", year)

    def get_scbpr(self, min_price, max_price):
        result = len(
            [
                lego_set
                for lego_set in self.set_list
                if lego_set.price >= min_price and lego_set.price <= max_price
            ]
        )
        return self.count_results_check(result, "price", f"{min_price} and {max_price}")

    def get_scbpc(self, min_pieces, max_pieces):
        result = len(
            [
                lego_set
                for lego_set in self.set_list
                if lego_set.pieces >= min_pieces and lego_set.pieces <= max_pieces
            ]
        )
        return self.count_results_check(
            result, "piece count", f"{min_pieces} and {max_pieces}"
        )

    def get_scbbst(self, built_status):
        result = [
            lego_set
            for lego_set in self.set_list
            if hasattr(lego_set, "built_status")
            and lego_set.built_status == built_status
        ]
        return self.query_results_check(result, "built status", built_status)

    def get_scpt(self, priority):
        result = [
            lego_set
            for lego_set in self.set_list
            if hasattr(lego_set, "priority") and lego_set.priority == priority
        ]
        return self.query_results_check(result, "priority", priority)

    def get_scty(self, type):
        result = len([lego_set for lego_set in self.set_list if lego_set.type == type])
        return self.count_results_check(result, "type", type)
