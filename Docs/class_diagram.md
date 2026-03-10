# OOP Class Diagram

```
Legoset
├── Attributes
│   ├── pieces (Integer)
│   ├── name (String)
│   ├── theme (String)
│   ├── set_num (Integer)
│   ├── year (Integer)
│   ├── price (Float)
│   └── type (String)
├── Methods
│   └── display()
│
├── OwnedLegoSet (inherits Legoset)
│   ├── Attributes
│   │   └── built_status (String)
│   └── Methods
│       ├── update_built_status(new_status)
│       └── display()
│
└── WantedLegoSet (inherits Legoset)
    ├── Attributes
    │   └── priority (String)
    └── Methods
        ├── update_priority(new_priority)
        └── display()

─────────────────────────────────────────

VaultManager
├── Attributes
│   └── set_list (List)
└── Methods
    ├── is_duplicate(set_num)
    ├── add_set(new_set)
    ├── rm_set(set_trm)
    ├── update_set_name/theme/year/price/pieces(set_num, value)
    ├── update_set_status(set_num, new_status)
    ├── update_set_priority(set_num, new_priority)
    ├── change_set_type(set_num)
    ├── get_sbn/sbnum/sbt/sby/sbpr/sbpc/sbst(filter)
    └── get_sc/scbt/scby/scbpr/scbpc/scbst(filter)

─────────────────────────────────────────

MenuPage
├── Attributes
│   ├── title (String)
│   └── options (List)

─────────────────────────────────────────

MenuDisplay
├── Attributes
│   ├── vault_manager (VaultManager)
│   ├── pages (List)
│   ├── current_page (Integer)
│   └── width (Integer)
└── Methods
    ├── display()
    ├── next_page()
    ├── prev_page()
    ├── go_to_page()
    └── run()

─────────────────────────────────────────

UpdateSetLogic
├── Attributes
│   ├── vault_manager (VaultManager)
│   └── set_num (Integer)
└── Methods
    ├── update_menu()
    ├── update_menu_owned()
    └── update_menu_wanted()

─────────────────────────────────────────

ErrorName (base exception class)
└── (see error_handler.py for all subclasses)
    e.g. NoSetsFoundError, MenuError, SetNameError,
         ThemeError, YearError, PriceError etc.

─────────────────────────────────────────

FieldInput
└── Methods
    └── get(prompt)

ValidateInput (inherits ErrorName handling)
├── Methods
│   ├── get(prompt)
│   └── validate(value)
└── (see error_handler.py and input_handler.py for all subclasses)
    e.g. SetNameInput, ThemeInput, YearInput,
         PriceInput, PieceInput, MenuInput etc.
```