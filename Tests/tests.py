"""
tests.py

Test suite for all .py files.
"""

import unittest
import app as apppy
from ProductionCode import data as datapy
from ProductionCode.filter import Filter as filterpy

class DataTests(unittest.TestCase):
    """ Test suite for ProductionCode/data.py """

    def setUp(self):
        """ Sets up the test suite. """
        datapy.Data.__init__()

class FilterTests(unittest.testCase):
    """ Test suite for ProductionCode/filter.py """

    def setUp(self):
        """ Sets up the test suite. """
        filterpy.__init__()

class AppTests(unittest.TestCase):
    """ Test suite for app.py """

    def setUp(self):
        """ Sets up the test suite. """
        apppy.initialize_data()

    def test__parse_ui_release_year_onward__normal(self):
        """ Tests app.parse_ui_release_year_onward() under 
        normal circumstances. """
        self.assertEqual(
            apppy.parse_ui_release_year_onward("2020"),
            2020
        )

    def test__parse_ui_release_year_onward__exception(self):
        """ Tests app.parse_ui_release_year_onward() when a year is 
        given that is not readable. """
        self.assertEqual(
            apppy.parse_ui_release_year_onward(
                "Not readable as an integer"
            ),
            0
        )

    def test__homepage(self):
        """ Ensures the homepage function returns the proper homepage. """
        with open('homepage.html', encoding="utf_8") as f:
            homepage = f.read()
        self.assertEqual(
            apppy.homepage(),
            homepage
        )
    
    def test__filterpage(self):
        """ Checks the filter page. """

if __name__ == "__main__":
    unittest.main()
