## Naming Conventions

- **Folders**  
  - Use `lowercase-kebab-case`  
  - Examples: `my-project`, `controllers`, `user-profile`

- **Files**  
  - Prefer `snake_case` for file names
  - Example: `user_model.py`

- **Components**  
  - Use `PascalCase`
  - Each folder contains its `.html`, `.css`, and `.py` files  
  - Examples: `ChartComponents/ChartComponent.py`

- **Variables**  
  - Use `snake_case`  
  - Examples: `user_data`, `load_user_data`

- **Functions**  
  - Use `camelCase`  
  - Examples: `userData()`, `loadUserData()`

- **Constants**  
  - Use `UPPER_CASE_WITH_UNDERSCORES`  
  - Example: `const API_BASE_URL = '...'`

---

## Coding Paradigm

This project follows a **Functional Programming** approach. Key principles include:

1. **Pure Functions**  
   - Functions should aim to produce the same output for the same input, without side effects.  
   - This helps improve testability and predictability.

2. **Immutability**  
   - Whenever possible, avoid mutating data structures. Create new objects or arrays instead of modifying existing ones in place.

3. **Declarative Code**  
   - Write code that focuses on **what** the program should accomplish rather than **how** it achieves it at every step.  
   - Emphasize readability and clear data transformations.

4. **Composition over Inheritance**  
   - Build functionality by combining smaller, specialized functions rather than using class inheritance or large, monolithic functions.

5. **Commenting**
   - Inline comments when needed only.
   - Keep variable and function names descriptive, even if it gets long, reducing the use of multiple inline commenting.
   - All functions should have doc. strings at the start of every function, e.g.,  (as seen below)

### IMPORTANT

6. **Strongly Typed**
   - Usage of the typing std. library in python as seen below (as seen below)

7. **Threading usage**
   - If you have to use async prog. in python use multi-threading instead
   - Both work based off the same concept with minimum code overhead

```
from typing import List, Tuple


def addNumbers(a: int, b: float) -> float:
    """
    Add two numeric values (int or float) and return the result.

    :param a: first operand, an int or float
    :param b: second operand, an int or float
    :return: the sum, preserving int or float as appropriate
    """
    return a + b
```

---

## Expected Proj. Struct.

```bash
project/

├── table1_logic.py
├── table2_logic.py
├── other_scripts.py
├── utils.py
├── app.py
├── .gitignore
├── readme.md
└── .env
```

By applying these guidelines, we aim to maintain consistency, reduce bugs, and keep the codebase easier to maintain.
