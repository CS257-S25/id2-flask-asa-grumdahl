import unittest
from ProductionCode import data as datapy
from ProductionCode.filter import Filter as filterpy

class TestSuite(unittest.TestCase):
    """ Testing area to ensure functions work before developing them. """

    def setUp(self):
        """ Sets up the test suite. """
        pass

    def test_turn_dataset_name_in_url_to_filepath(self):
        self.assertEqual("./Dummy_data/dummy_amazon.csv",filterpy.turn_dataset_name_in_url_to_filepath("amazon"))

if __name__ == "__main__":
    unittest.main()
