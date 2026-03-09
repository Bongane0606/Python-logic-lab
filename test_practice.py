# test_practice.py
import unittest
from practice import *
class TestPracticeFunctions(unittest.TestCase):

    # 1. STRING MANIPULATION
    def test_shout_text(self):
        self.assertEqual(shout_text("hello"), "HELLO!")
        self.assertEqual(shout_text("Hi"), "HI!")

    def test_count_letter_a(self):
        self.assertEqual(count_letter_a("Apple"), 1)
        self.assertEqual(count_letter_a("Banana"), 3)

    # 2. LIST & ARRAY LOGIC
    def test_find_first_element(self):
        self.assertEqual(find_first_element([10, 20, 30]), 10)
        self.assertIsNone(find_first_element([]))

    def test_double_list(self):
        self.assertEqual(double_list([1, 2, 3]), [2, 4, 6])
        self.assertEqual(double_list([0, -5]), [0, -10])

    # 3. MATHEMATICAL OPERATIONS
    def test_is_even(self):
        self.assertEqual(is_even(4), True)
        self.assertEqual(is_even(7), False)

    def test_sum_two_numbers(self):
        self.assertEqual(sum_two_numbers(10, 5), 15)
        self.assertEqual(sum_two_numbers(-1, 1), 0)

    # 4. DICTIONARY & FREQUENCY
    def test_get_value(self):
        test_dict = {"name": "Alice", "age": 25}
        self.assertEqual(get_value(test_dict, "name"), "Alice")
        self.assertEqual(get_value(test_dict, "job"), "Not Found")

    def test_create_simple_dict(self):
        self.assertEqual(create_simple_dict("color", "red"), {"color": "red"})

    # 5. SEARCHING & FILTERING
    def test_contains_negative(self):
        self.assertTrue(contains_negative([1, 2, -3, 4]))
        self.assertFalse(contains_negative([1, 2, 3]))

    def test_filter_over_ten(self):
        self.assertEqual(filter_over_ten([5, 12, 8, 20]), [12, 20])
        self.assertEqual(filter_over_ten([1, 2, 3]), [])

    # 6. MATRIX & 2D GRIDS
    def test_get_top_left(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(get_top_left(matrix), 1)

    def test_count_rows(self):
        self.assertEqual(count_rows([[1, 2], [3, 4]]), 2)
        self.assertEqual(count_rows([[1], [2], [3]]), 3)

    # 7. LOGIC & CONDITIONALS
    def test_can_vote(self):
        self.assertTrue(can_vote(18))
        self.assertFalse(can_vote(17))

    def test_simple_calculator(self):
        self.assertEqual(simple_calculator(10, 5, "add"), 15)
        self.assertEqual(simple_calculator(10, 5, "sub"), 5)

if __name__ == "__main__":
    unittest.main()