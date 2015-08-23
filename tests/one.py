
import sys
import say
sys.path.append('..')

import data, ask
import unittest

        
class TestAskFunctions(unittest.TestCase):
    """Тестирование ввода данных"""
    
    def setUp(self):
        pass
        
    def test_yesno(self):
        for answer in ["", "1", "y", "Yes", "111"]:
            with self.subTest("Test for Yes", answer=answer):
                self.assertTrue(ask.yesno(prompt="Yes?", default=True, input_func=lambda: answer))
        
        for answer in ["0", "n", "No", "000", "wtf", "1dg6seq112"]:
            with self.subTest("Test for No", answer=answer):
                self.assertFalse(ask.yesno(prompt="Yes?", default=True, input_func=lambda: answer))
        
    
    @unittest.skip("Fuck the numbers!")
    def test_number(self):
        """docstring for test_number"""
        ask.number("Number?", 100, input_func=lambda: "190")



if __name__ == "__main__":
    unittest.main()

    