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

A dedicated ```LegoSet``` class to define the properties of a set, and a Vault class to manage the list of objects.

</details>

<details>
<summary> CRUD Functionality</summary>

**C**reate: Add a new set (Number, Name, Theme, Pieces). \
\
**R**ead: List all sets currently in the vault. \
\
**U**pdate: Change the status of a set (e.g., "In Box" -> "Built"). \
\
**D**elete: Remove a set from the inventory.

</details>

<details>
<summary> File Reading</summary>

The system will use **JSON** to read and write data to a local file. This ensures the user's data remains after the program is closed.

</details>

<details>
<summary> Searching (Mid-tier Goal)</summary>
  
A feature to find specific sets by searching for keywords in the **Name** or **Theme** (e.g., searching "Star Wars" lists all matching sets).

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
ooomutils: For styling and fun.

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
Class: LegoSet
  Attributes:
    set_num (Integer): The official LEGO number.
    name (String): The name of the set.
    theme (String): The category (e.g., City, Technic).
    pieces (Integer): Number of parts.
  Methods:
    __str__(): Returns a formatted string for easy printing.
    update_status(): Toggles between "Built" and "In Box".
```
</details>

<details>
<summary> 2. vault_logic.py (The Manager)</summary>

```
Class: VaultManager
Attributes:
  sets_list (List): A list containing LegoSet objects.
Methods:
  add_set(lego_set_object): Adds a new object to the list.
  remove_set(set_num): Finds and removes a set.
  search_by_theme(keyword): Returns a filtered list.
  sort_by_pieces(): Reorders the list based on count.
```

</details>

<details>
<summary> 3. file_handler.py (Storage)</summary>

```
Functions:
  save_to_json(filename, data_list): Converts objects to dictionaries and saves to file.
  load_from_json(filename): Reads file and recreates objects.
```

</details>

<details>
<summary> 4. main.py (User Interface)</summary>
  
```
Functions:
  main_loop(): Captures user input and calls the appropriate function from VaultManager.
  display_menu(): Shows text options to the user.
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