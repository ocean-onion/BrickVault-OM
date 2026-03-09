# Project proposal and planning

## Project idea and purpose


<details>
<summary> What does your program do?</summary>

The brick vault will be a storage system for LEGO© collectors to log their sets and see details between each such as release date pieces, minifigures etc.

</details>

<details>
<summary> What problem does it solve?</summary>

It solves a the issue of centralised tracking of sets, will prevent duplication purchases and provide any easy to access to way to see all set details.

</details>

<details>
<summary> Who is the intended user?</summary>

The intend user for this application is LEGO© collecters or LEGO© store who wish to have detailed statistics on their sets.

</details>


<details>
<summary> Intended user interface?</summary>

Terminal based. This will allow the program to fully focused on functionality rather than aesthetics.

</details>


---


## Feature breakdown


<details>
<summary> Class system</summary>

A dedicated LegoSet base class to define the properties shared by all sets, with two subclasses to handle specific types:

- OwnedLegoSet: Extends Legoset with a built_status field to track whether the set has been built.
- WantedLegoSet: Extends Legoset with a priority field to track how much the user wants the set.

A VaultManager class manages the list of objects and handles all CRUD and search operations.

</details>

<details>
<summary> CRUD Functionality</summary>

**C**reate: Add a new owned or wanted Lego set with all details. \
\
**R**ead: Display all sets, or sets filtered by type, theme, year, price, pieces, status or priority. \
\
**U**pdate: Change any field on an existing set including name, theme, year, price, pieces, built status or priority. \
\
**D**elete: Remove a set from the vault by name or set number.

</details>

<details>
<summary> File Reading</summary>

The system uses **JSON** to read and write data to local files. Sets are saved to a master sets.json file and automatically split into jsons/owned_sets.json and jsons/wanted_sets.json for organised storage. This ensures the user's data remains after the program is closed.

</details>

<details>
<summary> Searching (Mid-tier Goal)</summary>
  
Search by name or set number, theme (**fuzzy matching**), year, price range, piece count, built status, and priority.

</details>

<details>
<summary> Sorting (Mid-tier Goal)</summary>

Ability to view the list sorted by **Piece Count** and other factors, helping the user analyze their most favourited items.

</details>

<details>
<summary> Statistics (Stretch Goal)</summary>
  
A ```Dashboard``` function that calculates summary statistics, such as the total number of ```sets```, ```total piece count```, and the estimated ```total value``` of the collection.

</details>

<details>
<summary> Data Export (Stretch Goal)</summary>
  
A feature to export the collection to a readable text file (my_collection.txt) so the user can print a physical checklist of their inventory.

</details>


---


## Technology Stack


<details>
<summary> Programming Language</summary>
  
```Python 3.10+```

</details>

<details>
<summary> Libraries & Modules</summary>
  
json: For data serialization (saving objects to text). \
os: For checking if files exist and handling file paths. \
datetime: To record the date a set was added to the collection. \
sys: For exiting the program cleanly. \
ooomutils: For styling and fun. \
thefuzz: Improved searching functionality.

</details>

<details>
<summary> Development Tools</summary>
  
IDE: Replit.\
Version Control: Replit/Github

</details>


---


## Class Design (OOP Architecture)

<details>
<summary> 1. models.py (The Object)</summary>
  
```
Class: Legoset (Base Class)
  Attributes:
    set_num (Integer): The official LEGO number.
    name (String): The name of the set.
    theme (String): The category (e.g., City, Technic).
    pieces (Integer): Number of parts.
    year (Integer): The year the set was released.
    price (Float): The price of the set.
    type (String): Whether the set is owned or wanted.
  Methods:
    display(): Displays set attributes in a formatted ASCII box.

Class: OwnedLegoSet (Inherits Legoset)
  Attributes:
    built_status (String): Whether the set has been built.
  Methods:
    update_built_status(new_status): Updates the built status.
    display(): Overrides base display to include built status.

Class: WantedLegoSet (Inherits Legoset)
  Attributes:
    priority (String): How much the user wants the set.
  Methods:
    update_priority(new_priority): Updates the priority.
    display(): Overrides base display to include priority.
```
</details>

<details>
<summary> 2. vault_logic.py (The Manager)</summary>

```
Class: VaultManager
Attributes:
  set_list (List): A list containing Legoset objects.
Methods:
  add_set(lego_set): Adds a new set, checks for duplicates.
  rm_set(set_trm): Finds and removes a set by name or number.
  update_set_name/theme/year/price/pieces(set_num, value): Updates a field.
  update_set_status(set_num, new_status): Updates built status.
  update_set_priority(set_num, new_priority): Updates priority.
  change_set_type(set_num): Switches a set between owned and wanted.
  get_sbn/sbnum/sbt/sby/sbpr/sbpc/sbst(filter): Returns filtered sets.
  get_sc/scbt/scby/scbpr/scbpc/scbst(filter): Returns set counts.
```

</details>

<details>
<summary> 3. file_handler.py (Storage)</summary>

```
Functions:
save_to_json(vault_manager, filename): Saves all sets to a single JSON file.
load_from_json(vault_manager, filename): Reads file and recreates the correct
  subclass (OwnedLegoSet or WantedLegoSet) based on the type field.
  Handles missing or empty files gracefully.
update_split_files(vault_manager): Splits the set list into
  owned_sets.json and wanted_sets.json and saves all sets to sets.json.
```

</details>

<details>
<summary> 4. main.py (User Interface)</summary>
  
```
Functions:
  DoLoadingScreen(): Displays the loading screen on startup.
  main(): Runs the main loop, handles menu navigation and calls
    the appropriate VaultManager functions based on user input.
```

</details>


---


## Legal & Ethical Considerations


**1. What could go wrong if this was released publicly?**
*   **Data Integrity & Liability:** If the software contains bugs (e.g., a flaw in the "save" function), it could corrupt or delete a user's `inventory.json` file. For a serious collector with thousands of sets logged, this represents a significant loss of time and data. If released publicly, users might expect a warranty or hold the developer liable for this data loss.
*   **Mitigation:** The software would need to be released with a strict "End User License Agreement" (EULA) stating that the software is provided "as is" and the developer is not responsible for data loss.

**2. What data privacy or security issues might exist?**
*   **Unencrypted Local Storage:** The application stores the user's collection data, including the total financial value, in a plain text JSON file. This file is not encrypted.
*   **Security Risk:** If a malicious actor gained access to the user's computer, they could open this file to see exactly which expensive sets the user owns and their total value, potentially making the user a target for theft.
*   **Privacy:** Unlike cloud apps, no data is sent to the internet, which is a privacy benefit. However, the lack of cloud backup means if the user's hard drive fails, their data is lost permanently unless they manually back it up.

**3. Any intellectual property concerns?**
*   **LEGO® Trademark:** "LEGO" is a registered trademark of the LEGO Group. This application must not infringe on that trademark by appearing to be an official product.
*   **Solution:** The application is named "BrickVault" rather than "LEGO Manager" to avoid confusion. The documentation explicitly states: *"LEGO® is a trademark of the LEGO Group of companies which does not sponsor, authorize or endorse this project."*
*   **Code Plagiarism:** As a student project, all code logic (sorting algorithms, class structures) must be original work or properly cited to avoid academic misconduct and copyright infringement of existing open-source inventory tools.