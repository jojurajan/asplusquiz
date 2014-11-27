import unittest
from consecutive import Consecutive


class ConsecutiveTest(unittest.TestCase):

    def test_max_consecutive_characters_should_return_a_list(self):
        c = Consecutive("aaddddffffaa")
        self.assertIsInstance(c.max_consecutive_characters(), list)

    def test_cat_dog___(self):
        c = Consecutive("cat dog ___")
        self.assertEqual(c.max_consecutive_characters(), ['_'])

    def test_aabbaabbbaa(self):
        c = Consecutive("aabbaabbbaa")
        self.assertEqual(['b'], c.max_consecutive_characters())

    def test_aabaa(self):
        c = Consecutive("aabaa")
        self.assertEqual(['a'], c.max_consecutive_characters())

    def test_aaddddffffaa(self):
        c = Consecutive("aaddddffffaa")
        self.assertEqual(['d', 'f'], c.max_consecutive_characters())

    def test_sort_order(self):
        c = Consecutive("bbaa")
        self.assertEqual(['a', 'b'], c.max_consecutive_characters())

    def test_not_highest_letter_most_common(self):
        c = Consecutive("aaaaaaaaaaaaaaaaaaaaaaaaaaaazbb")
        self.assertEqual(['a'], c.max_consecutive_characters())

    def test_multiple_character_instances(self):
        c = Consecutive("aaabba")
        self.assertEqual(['a'], c.max_consecutive_characters())


if __name__ == '__main__':
    unittest.main()
