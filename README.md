# Python Logic Lab 🧠🐍

A collection of beginner-friendly Python functions that demonstrate core programming concepts such as:

* String manipulation
* List operations
* Mathematical logic
* Dictionary usage
* Searching and filtering
* Matrix handling
* Conditional logic

This project was created as a programming skills test to demonstrate understanding of fundamental Python concepts.

---

# Project Structure

The project consists of multiple functions grouped by programming concepts.

---

# 1. String Manipulation

### `shout_text(s: str) -> str`

**Purpose:**
Converts a string to uppercase and adds an exclamation mark.

**Logic:**

1. Convert the input string to uppercase using `.upper()`.
2. Add `"!"` to the end.
3. Return the new string.

**Example**

```python
shout_text("hello")
```

Output

```
HELLO!
```

---

### `count_letter_a(s: str) -> int`

**Purpose:**
Counts how many times the letter **"a"** appears in a string (case-insensitive).

**Logic:**

1. Loop through each character in the string.
2. Check if the character is `"a"` or `"A"`.
3. Increment a counter when a match is found.
4. Return the total count.

---

# 2. List & Array Logic

### `find_first_element(nums: list)`

**Purpose:**
Returns the first element in a list.

**Logic:**

1. If the list is empty, return `None`.
2. Otherwise return the element at index `0`.

---

### `double_list(nums: list[int]) -> list[int]`

**Purpose:**
Creates a new list where each number is doubled.

**Logic:**

1. Create an empty list.
2. Loop through each number.
3. Multiply each value by `2`.
4. Append it to the new list.
5. Return the new list.

**Example**

```python
double_list([1,2,3])
```

Output

```
[2,4,6]
```

---

# 3. Mathematical Operations

### `is_even(n: int) -> bool`

**Purpose:**
Checks whether a number is even.

**Logic:**

1. Use the modulus operator `%`.
2. If `n % 2 == 0`, the number is even.
3. Return `True` if even, otherwise `False`.

---

### `sum_two_numbers(a: int, b: int) -> int`

**Purpose:**
Returns the sum of two numbers.

**Logic:**

1. Add the two values.
2. Return the result.

---

# 4. Dictionary & Frequency

### `get_value(d: dict, key: str)`

**Purpose:**
Retrieves a value from a dictionary.

**Logic:**

1. Loop through dictionary keys.
2. If the key matches the requested key, return the value.
3. If the key does not exist, return `"Not Found"`.

---

### `create_simple_dict(key: str, value: any) -> dict`

**Purpose:**
Creates a dictionary with one key-value pair.

**Logic:**

1. Use dictionary syntax `{key: value}`.
2. Return the created dictionary.

---

# 5. Searching & Filtering

### `contains_negative(numbers: list[int]) -> bool`

**Purpose:**
Checks if a list contains any negative numbers.

**Logic:**

1. Loop through the list.
2. If a number is less than `0`, return `True`.
3. If none are negative, return `False`.

---

### `filter_over_ten(numbers: list[int]) -> list[int]`

**Purpose:**
Returns only numbers greater than `10`.

**Logic:**

1. Create an empty list.
2. Loop through the numbers.
3. If a number is greater than `10`, add it to the new list.
4. Return the filtered list.

---

# 6. Matrix & 2D Grids

### `get_top_left(matrix: list[list[int]]) -> int`

**Purpose:**
Returns the value in the **top-left corner** of a 2D matrix.

**Logic:**

1. Access row `0`.
2. Access column `0`.
3. Return `matrix[0][0]`.

---

### `count_rows(matrix: list[list[int]]) -> int`

**Purpose:**
Counts the number of rows in a matrix.

**Logic:**

1. Use the `len()` function.
2. Return the length of the matrix.

---

# 7. Logic & Conditionals

### `can_vote(age: int) -> bool`

**Purpose:**
Checks if someone is old enough to vote.

**Logic:**

1. If age is `18` or greater, return `True`.
2. Otherwise return `False`.

---

### `simple_calculator(a: int, b: int, operation: str) -> int`

**Purpose:**
Performs a basic calculation.

**Supported Operations**

* `"add"` → addition
* `"sub"` → subtraction

**Logic:**

1. Check the operation string.
2. If `"add"` return `a + b`.
3. If `"sub"` return `a - b`.

---

# Technologies Used

* Python 3

---

# Purpose of the Project

This project demonstrates understanding of:

* Python syntax
* Loops
* Conditionals
* Functions
* Lists and dictionaries
* Basic algorithmic thinking

It is intended as a **practice and learning repository** for improving core Python programming skills.

---
