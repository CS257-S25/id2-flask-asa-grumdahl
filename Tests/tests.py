import unittest
from ProductionCode import data as Data
from ProductionCode.filter import Filter

class TestStuff(unittest.TestCase):
    """ Testing area to ensure functions work before developing them. Only sufficiently relevant tests will be kept. """

    def test_turn_dataset_name_in_url_to_filepath(self):
        self.assertEqual("./Dummy_data/dummy_amazon.csv",app.turn_dataset_name_in_url_to_filepath("amazon"))

if __name__ == "__main__":
    unittest.main()
