# Test Table

## Core Functions Tests

| Test ID | What I Tested | Input or Steps | Expected Result | Actual Result | Pass or Fail | Notes |
|---------|--------------|----------------|-----------------|---------------|--------------|-------|
| T01 | Add a valid owned set | set_num: 75192, name: Millennium Falcon, theme: Star Wars, price: 849.99, year: 2017, pieces: 7541, status: built | "Lego set added successfully!" and set saved to owned_sets.json | As expected | Pass | |
| T02 | Change owned set to wanted | set_num: 75192 on existing owned set | Set type changes to wanted, built_status removed, priority set to medium, saved to wanted_sets.json | As expected | Pass | |
| T03 | Display all sets on empty vault | Page 1, choice 3 with no sets loaded | NoSetsFoundError raised | As expected | Pass | |
| T04 | Update theme of a wanted set | Page 2, choice 4, set_num: 75192, new theme: Star Wars | Theme updates and saves to wanted_sets.json | TypeError: update_menu_wanted() takes 1 positional argument but 2 were given | Fail | Fixed by properly instantiating UpdateSetLogic |
| T05 | Add duplicate set | set_num: 75192 when 75192 already exists | "Set 75192 already exists in the vault." | As expected | Pass | |
| T06 | Invalid price input | Enter "100" with no decimal point | PriceError raised, re-prompts user | As expected | Pass | Invalid input test |
| T07 | Invalid year input | Enter "1800" as year | YearError raised, re-prompts user | As expected | Pass | Invalid input test |
| T08 | Search by name with fuzzy match | Search "millenium falcn" (typo) | Millennium Falcon returned | As expected | Pass | thefuzz token_set_ratio > 70 |
| T09 | Save and reload set data | Add set, close program, reopen | Set still present after reload | As expected | Pass | File handling test |
| T10 | Load from missing JSON file | Delete owned_sets.json, run program | File created fresh, empty list loaded | As expected | Pass | File handling edge case |