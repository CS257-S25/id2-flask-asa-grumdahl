from app import *
import unittest

class TestStuff(unittest.testCase)
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects = True)
        self.assertEqual(b'fermented greenland shark', response.data)