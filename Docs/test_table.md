# Test Table

## Core Functions Tests

| Test ID | Test Description | Input or Steps | Expected Result | Actual Result | Pass or Fail | Notes |
|---------|-----------------|----------------|-----------------|---------------|--------------|-------|
| T01 | Add a valid owned set | set_num: 75192, name: Millennium Falcon, theme: Star Wars, price: 849.99, year: 2017, pieces: 7541, status: built | "Lego set added successfully!" and set saved to owned_sets.json | "Lego set added successfully!" and set saved to owned_sets.json | Pass | |
| T02 | Change owned set to wanted | set_num of existing owned set (7541) | Set type changes to wanted, built_status removed, priority set to mid, saved to wanted_sets.json | Set type changed to wanted, built_status removed, priority set to mid, saved to wanted_sets.json | Pass | |