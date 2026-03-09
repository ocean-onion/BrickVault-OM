# Development Log

```Log_01```

## Date: ```Sun 1/3/26```

### 1. Task / Goal

```
Complete planning, timeline and create inital files.
```

### 2. Reason

```
Required by task and important first step in development.
```

### 3. ~~Problems Encountered~~

```

```

### 4. ~~Solutions~~

```

```

### 5. Tools Used

```
Replit
```

### 6. ~~Evidence~~

```

```

### 7. Time Spent

```
120 minutes
```

---

```Log_02```

## Date: ```Thu 5/3/26```

### 1. Task / Goal

```
Start coding. Set up vault_logic.py and models.py, including search query results, add and removing sets functionality.
```

### 2. Reason

```
Is all functions required for main to run eventually
```

### 3. Problems Encountered

```
Didn't know how to make an advanced search system to get responses if search query is spelt wrong.
```

### 4. Solutions

```
Installed package thefuzz to use their libaray as it allows so search query accuracy functionality.
```

### 5. Tools used

```
Google AI studio
```

### 6. Evidence

* #### Chat link: ```https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%2213VQPOv8Y2qxV3G9ac6Rsy-pLbhHINfK1%22%5D,%22action%22:%22open%22,%22userId%22:%22105489606694128074321%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing```

* #### Evidence video/photo file path: 
```Docs/Evidence/Log_2_Evid_1.mov```

### 7. Time Spent

```
120 Minutes
```

---


```Log_03```

## Date: ```Sat 7/3/26```

### 1. Task / Goal

```
Refactor input validation, fix circular import and implement ValidatedInput base class.
```

### 2. Reason

```
Input classes had duplicate try/except everywhere and the while True loops werent actually looping because the return was in the wrong place.
```

### 3. Problems Encountered

```
Circular import between error_handler.py and input_handler.py was crashing the program. SetSearchInput was prompting twice because SetNameInput was calling FieldInput.get() again. Every input class had the same try/except copy pasted. Didnt know which string method to use for alphabet checking. Realised isalpha() wouldnt work because set names like Batman 2 Car have numbers in them.
```

### 4. Solutions

```
Made a error_name_logic.py file to fix the circular import. Changed SetSearchInput to call SetNameInput.validate() instead of SetNameInput.get() so it reuses the value already gotten. Made ValidatedInput class that handles the while True loop and try/except so every input class just raises and returns without duplicating logic. Each class now only defines a validate() method with its own rules. Looked at w3schools string methods reference to find the right method. Switched from isalpha() to isalnum() to allow numbers in set names.
```

### 5. Tools Used

```
Replit, Claude AI, Google AI Studio
```

### 6. Evidence

* #### link: ```https://www.w3schools.com/python/python_ref_string.asp```
* #### Evidence video/photo file path:

```
Docs/Evidence/Screen_Recording_2026-03-06_at_10_30_36_am.mov
```

### 7. Time Spent

```
180 Minutes
```


---


```Log_04```

## Date: ```Sat 7/3/26```

### 1. Task / Goal

```
Fix VaultManager error handling, fix JSON saving and build the Legoset display method.
```

### 2. Reason

```
VaultManager methods were just returning empty lists with no error and rm_set wasnt raising anything when the set wasnt found.
```

### 3. Problems Encountered

```
rm_set was returning None instead of raising NoSetsFoundError. JSON was saving ™ and © as \u2122 unicode escapes instead of the actual symbols. No standard way to check empty results across all vault methods.
```

### 4. Solutions

```
Added query_results_check and count_results_check to VaultManager so all methods use the same check instead of repeating if not result everywhere. Fixed rm_set to raise NoSetsFoundError after the loop. Added ensure_ascii=False to json.dump to fix the unicode issue. Built a __str__ display method in Legoset with an ASCII box format.
```

### 5. Tools Used

```
Replit, Claude AI, Google AI Studio
```

### 6. Evidence

* #### Evidence video/photo file path:

```
Docs/Evidence/Log_4_Evid_1.mov
Docs/Evidence/Log_4_Evid_2.mov
Docs/Evidence/Log_4_Evid_3.mov
```

### 7. Time Spent

```
300 Minutes
```


---


```Log_05```

## Date: ```Sun 8/3/26```

### 1. Task / Goal

```
Fix SetSearchInput not returning an integer, implement MenuDisplay class with page navigation and integrate MenuInput into the menu system.
```

### 2. Reason

```
SetSearchInput was returning a string instead of an int so isinstance check in main wasnt working and the menu had no validation for invalid inputs.
```

### 3. Problems Encountered

```
SetSearchInput was returning sfs as a string so isinstance(sfs, int) was always False and it was calling get_sbn instead of get_sbnum. MenuDisplay wasnt using MenuInput so invalid choices like h and k were crashing the program. FieldInput wasnt imported in error_handler.py causing a NameError.
```

### 4. Solutions

```
Changed SetSearchInput.validate to return int(sfs) instead of sfs. Rewrote MenuInput to use FieldInput so it could accept both letters and numbers. Integrated MenuInput into MenuDisplay.run() so all input goes through proper validation. Fixed the FieldInput import in error_handler.py.
```

### 5. Tools Used

```
Replit, Claude AI
```

### ~~6. Evidence~~


```
```

### 7. Time Spent

```
240 Minutes
```

---

```Log_06```

## Date: ```Mon 9/3/26```

### 1. Task / Goal

```
Implement inheritance into the project to meet assignment requirements and fix bugs that arose from the refactor.
```

### 2. Reason

```
Assignment requires proof of inheritance usage. Single Legoset class was not demonstrating OOP inheritance properly and was causing crashes when loading JSON because the base class didnt accept fields like status and priority.
```

### 3. Problems Encountered

```
Didnt know how to implement inheritance into the existing project. Single Legoset class couldnt accept status and priority fields causing TypeError on load. built_status assigned from undefined variable in OwnedLegoSet.__init__. **set passing built-in type instead of loop variable in load_from_json. get_sbst referencing wrong attribute name. save_to_json used throughout but split file system required update_split_files. type and priority not defined when creating sets in main. vault_manager local to display() so MenuDisplay and main() were not sharing the same object. for loop indentation printing navigation options after every menu item. update_menu_wanted nested inside update_menu_owned. update_menu called in __init__ but didnt exist. StatusInput referenced but never defined. SetNameInput and ThemeInput catching their own errors preventing ValidateInput retry loop. load_from_json crashing on missing or empty JSON files.
```

### 4. Solutions

```
Restructured models.py into a proper inheritance hierarchy with Legoset as the base class and OwnedLegoSet and WantedLegoSet as subclasses each with their own unique attributes and display methods. Updated load_from_json to check the type field and create the correct subclass instead of always creating a base Legoset. Fixed all bugs that arose from the refactor including built_status assignment, **legoset fix, attribute name fixes, save function replacement, hardcoded type values, shared vault_manager via self.vault_manager, for loop indentation, update_menu_wanted dedent, update_menu creation, StatusInput to BuiltStatusInput, removed try/except from validate methods, and added file existence checks to load_from_json.
```

### 5. Tools Used

```
Replit, Claude AI, ChatGPT
```

### 6. Evidence


* #### Evidence video/photo file path:

```
Docs/Evidence/Log_6_Evid_1.mov
```

### 7. Time Spent

```
360 Minutes
```