import os
import unittest
from app_db import *

class AppDBTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        d = DB.data
        print(d)
        self.assertIsNotNone(d)

    def test_fetch_record(self):
        r = DB.fetch(0)
        print r
        self.assertIsNotNone(r)


if __name__ == '__main__':
    unittest.main()
