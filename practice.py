# --- 1. STRING MANIPULATION ---

def shout_text(s: str) -> str:
    """Requirement: Convert the entire string to uppercase and add an exclamation mark."""
    new_text = s.upper()
    return f"{new_text}!"
print(shout_text("HEllO"))

def count_letter_a(s: str) -> int:
    """Requirement: Count how many times the letter 'a' (case-insensitive) appears."""
    letter = "aA"
    total = 0
    for i in s:
        if i in letter:
            total = total + 1
    return total

# --- 2. LIST & ARRAY LOGIC ---

def find_first_element(nums: list):
    """Requirement: Return the first element of the list. If empty, return None."""
    for i in nums:
        if i == []:
            return None
        else:
            return nums[0]

def double_list(nums: list[int]) -> list[int]:
    """Requirement: Return a new list where every number is multiplied by 2."""
    new_list = []
    for i in nums:
        multiply = i * 2
        new_list.append(multiply)
    return new_list



# --- 3. MATHEMATICAL OPERATIONS ---

def is_even(n: int) -> bool:
    """Requirement: Return True if the number is even, False if it is odd."""
    if n % 2 == 0:
        return True
    return False
print(is_even(7))

def sum_two_numbers(a: int, b: int) -> int:
    """Requirement: Return the sum of a and b."""
    return a + b
print(sum_two_numbers(10,5))


# --- 4. DICTIONARY & FREQUENCY ---

def get_value(d: dict, key: str):
    """Requirement: Return the value for the given key. If key is missing, return "Not Found"."""
    for k in d:
        if k == key:
            return d[k]
    return "Not Found"

def create_simple_dict(key: str, value: any) -> dict:
    """Requirement: Take a key and a value and return them as a single-item dictionary."""
    return {key:value}
print(create_simple_dict("color", "red"))

        


# --- 5. SEARCHING & FILTERING ---

def contains_negative(numbers: list[int]) -> bool:
    """Requirement: Return True if any number in the list is less than 0."""
    for i in numbers:
        if i < 0:
            return True
    return False

def filter_over_ten(numbers: list[int]) -> list[int]:
    """Requirement: Return a list containing only the numbers that are greater than 10."""
    greater = []
    for i in numbers:
        if i > 10 :
            greater.append(i)
    return greater
print(filter_over_ten([5, 12, 8, 20]))

# --- 6. MATRIX & 2D GRIDS ---



def get_top_left(matrix: list[list[int]]) -> int:
    """Requirement: Given a 2D list (matrix), return the element at row 0, column 0."""
    return matrix[0][0]

def count_rows(matrix: list[list[int]]) -> int:
    """Requirement: Return the total number of rows in the matrix."""
    return len(matrix)


# --- 7. LOGIC & CONDITIONALS ---

def can_vote(age: int) -> bool:
    """Requirement: Return True if age is 18 or older, otherwise return False."""
    if age >= 18:
        return True
    return False

def simple_calculator(a: int, b: int, operation: str) -> int:
    """Requirement: If operation is "add", return a+b. If "sub", return a-b."""
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b

