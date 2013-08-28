#! /usr/bin/python
#run python -m chardetails.tests.chardetails_test from root directory
#of the repository
import unittest
from chardetails import getInstance


class TestChardetails(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_info(self):
        self.assertEqual('Shows the Unicode Character Details of a given character',
                         self.instance.get_info())

    def test_english_alphabets(self):
        self.assertEqual(self.instance.getdetails(u'AB')[u'A']['HTML Entity'],
                         '65')


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TransliterationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
