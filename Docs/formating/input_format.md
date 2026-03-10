# Formatting Guide

## JSON File Formats

### owned_sets.json
```json
[
    {
        "pieces": 7541,
        "name": "millennium_falcon",
        "theme": "star-wars",
        "set_num": 75192,
        "year": 2017,
        "price": 849.99,
        "type": "owned",
        "built_status": "built"
    }
]
```

### wanted_sets.json
```json
[
    {
        "pieces": 4784,
        "name": "imperial_star_destroyer",
        "theme": "star-wars",
        "set_num": 75252,
        "year": 2019,
        "price": 699.99,
        "type": "wanted",
        "priority": "high"
    }
]
```

### sets.json
```json
[
    {
        "pieces": 7541,
        "name": "millennium_falcon",
        "theme": "star-wars",
        "set_num": 75192,
        "year": 2017,
        "price": 849.99,
        "type": "owned",
        "built_status": "built"
    },
    {
        "pieces": 4784,
        "name": "imperial_star_destroyer",
        "theme": "star-wars",
        "set_num": 75252,
        "year": 2019,
        "price": 699.99,
        "type": "wanted",
        "priority": "high"
    }
]
```

---

## Input Formatting Rules

### Set Number
```
Type    : Integer
Format  : Digits only
Example : 75192
Invalid : 75192.1, ABC123
```

### Set Name
```
Type    : String
Format  : Alphanumeric, spaces, hyphens, underscores,
          commas, &, ™, ©, ®, ℗, $, % allowed
Example : Ferrari F2004 & Michael Schumacher
Invalid : Names with other special characters e.g. @, !, ?
Notes   : Stored internally with spaces replaced by underscores
          e.g. "Millennium Falcon" → "millennium_falcon"
```

### Theme
```
Type    : String
Format  : Alphanumeric, spaces, hyphens, underscores,
          commas, &, ™, ©, ®, ℗, $, % allowed
Example : Star Wars
Invalid : Themes with other special characters e.g. @, !, ?
Notes   : Stored internally with spaces replaced by hyphens
          e.g. "Star Wars" → "star-wars"
```

### Year
```
Type    : Integer
Format  : 4 digit year between 1949 and current year
Example : 2017
Invalid : 1800, 2099, abc
```

### Price
```
Type    : Float
Format  : Must include decimal point
Example : 849.99
Invalid : 849, abc
```

### Pieces
```
Type    : Integer
Format  : Digits only
Example : 7541
Invalid : 7541.5, abc
```

### Built Status
```
Type    : String
Format  : Letters only
Example : built, unbuilt
Invalid : 123, built1
```

### Priority
```
Type    : String
Format  : Letters only
Example : high, medium, low
Invalid : 123, high1
```