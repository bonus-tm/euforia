
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
        
    
    def test_number(self):
        num = ask.number("Number?", 100, input_func=lambda: "90", try_once=True)
        self.assertEqual(num, 90)


    def test_corn(self):
        max = 1000
        for answer in ["110 230", "110,  230", "  110 -   230.   ", "110. 230. "]:
            with self.subTest("Test corn", answer=answer):
                [food, seed] = ask.corn(max, input_func=lambda: answer, try_once=True)
                self.assertTrue(food == 110 and seed == 230)
    
    def test_corn_food_not_enough(self):
        max = 1000
        for answer in ["1100 230", "1100,  230", "  1100 -   230.   ", "1100. 230. "]:
            with self.subTest("Test corn more food than max", answer=answer):
                [food, seed] = ask.corn(max, input_func=lambda: answer, try_once=True)
                self.assertTrue(food < 0 and seed < 0)
    
    def test_corn_seed_not_enough(self):
        max = 1000
        for answer in ["950 230", "950,  230", "  950 -   230.   ", "950. 230. "]:
            with self.subTest("Test corn more food than max", answer=answer):
                [food, seed] = ask.corn(max, input_func=lambda: answer, try_once=True)
                self.assertTrue(food == 950 and seed == 50)
    


if __name__ == "__main__":
    unittest.main()

    