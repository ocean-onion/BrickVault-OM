# Test Table

## Core Functions Tests

| Test ID | Test Description | Input or Steps | Expected Result | Actual Result | Pass or Fail | Notes |
|---------|-----------------|----------------|-----------------|---------------|--------------|-------|
| T01 | Add a valid owned set | set_num: 75192, name: Millennium Falcon, theme: Star Wars, price: 849.99, year: 2017, pieces: 7541, status: built | "Lego set added successfully!" and set saved to owned_sets.json | "Lego set added successfully!" and set saved to owned_sets.json | Pass | |
| T02 | Change owned set to wanted | set_num of existing owned set (7541) | Set type changes to wanted, built_status removed, priority set to mid, saved to wanted_sets.json | Set type changed to wanted, built_status removed, priority set to mid, saved to wanted_sets.json | Pass | |
| T03 | Display all sets in owned sets json | On page 1: choice: 3 | [2026-03-12 01:29:44.043356] [LOG]: A NoSetsFoundError has occurred \n There are no sets in the vault with sets all. | [2026-03-12 01:29:44.043356] [LOG]: A NoSetsFoundError has occurred n\ There are no sets in the vault with sets all. | Pass | |
| T04 | Update theme of a wanted set | On page 2: choice 4, set_num: 75192 | Update menu displays, theme updates successfully and saves to wanted_sets.json | Set displayed correctly then TypeError: UpdateSetLogic.update_menu_wanted() takes 1 positional argument but 2 were given | Fail | UpdateSetLogic not instantiated correctly, set_num not passing correctly |