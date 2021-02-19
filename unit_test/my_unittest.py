import unittest

import sys
sys.path.append(".")
from unit_test_module.mongochat import MyMongochat


class Testmongochat(unittest.TestCase):
   
    def test_lower(self):
        
        """
        Test lower function
        """
        message_test = "what is the difference between machine learning and deep learning?"
        mongoc = MyMongochat(None)
        result = mongoc._lower(message_test,"ai")
        self.assertEqual(result,"learn machin differ deep")

if __name__ == '__main__':
    unittest.main()
