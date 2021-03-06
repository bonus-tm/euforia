import sys, unittest

sys.path.append('..')
from say import Say
from data import Data
# from info import Info
from ask import Ask


        
class TestAskFunctions(unittest.TestCase):
    """Тестирование ввода данных"""
    
    def setUp(self):
        self.say = Say(lambda *ar, **kw: False)
        self.ask = Ask(self.say)
    
    # рандом
    def test_dice(self):
        probability = 90
        self.ask.random_int_func = lambda *args: 10
        self.assertTrue(self.ask.dice(probability))
        
        self.ask.random_int_func = lambda *args: 99
        self.assertFalse(self.ask.dice(probability))
    
    
    # фигня
    def test_rand(self):
        self.assertIsInstance(self.ask.rand(990, 1000), int)
        self.assertIsInstance(self.ask.frand(0.1, 10), float)
    
    
    # да-нет
    def test_yesno(self):
        for answer in ["", "1", "y", "Yes", "yes", "YES", "111"]:
            with self.subTest("Test for Yes", answer=answer):
                self.ask.input_func = lambda: answer.lower()
                self.assertTrue(self.ask.yesno(prompt="Yes?", default=True),
                                msg="'{:s}' should be Yes".format(answer))
        
        for answer in ["0", "n", "No", "000", "wtf", "1dg6seq112"]:
            with self.subTest("Test for No", answer=answer):
                self.ask.input_func = lambda: answer.lower()
                self.assertFalse(self.ask.yesno(prompt="Yes?", default=True),
                                msg="'{:s}' should be No".format(answer))
        
    
    # ввод чисел
    def test_good_number(self):
        max = 100
        for i in ["56", " 56   "]:
            with self.subTest("Good numbers", i=i):
                self.ask.input_func = lambda: i
                num, error, msg = self.ask.number("Number?", max)
                self.assertEqual(num, 56, msg="Got wrong number")
                self.assertFalse(error, msg="'error' param isn't False")
                self.assertEqual(msg, "", msg="'msg' param not empty string")
                
    def test_bad_number(self):
        max = 100
        for i in ["56.6", " 56,5   ", "56 56 ", "wtf ", "56wtf", "wtf56"]:
            with self.subTest("Good numbers", i=i):
                self.ask.input_func = lambda: i
                num, error, msg = self.ask.number("Number?", max)
                self.assertEqual(num, -1, msg="Is '{:s}' number?".format(i))
                self.assertTrue(error, msg="'error' param is False, should be True")
                self.assertEqual(msg, "Это не число!", msg="'msg' is wrong")
    
    def test_number_more_than_max(self):
        max = 100
        error_msg = "more than max"
        for i in ["120", " 120   "]:
            with self.subTest("Number more than max", i=i):
                self.ask.input_func = lambda: i
                num, error, msg = self.ask.number("Number?", max, error_msg=error_msg)
                self.assertEqual(num, max, msg="Is '{:s}' a number?".format(i))
                self.assertTrue(error, msg="'error' param is False, should be True")
                self.assertEqual(msg, error_msg, msg="'msg' is wrong")
    

    # ввод распределения зерна - перенести в маркет
    @unittest.skip("Corn moved to Disrtibute class")
    def test_corn(self):
        max = 1000
        for answer in ["110 230", "110,  230", "  110 -   230.   ", "110. 230. "]:
            with self.subTest("Test corn", answer=answer):
                [food, seed] = self.ask.corn(max, input_func=lambda: answer, try_once=True)
                self.assertTrue(food == 110 and seed == 230)
    
    @unittest.skip("Corn moved to Disrtibute class")
    def test_corn_food_not_enough(self):
        max = 1000
        for answer in ["1100 230", "1100,  230", "  1100 -   230.   ", "1100. 230. "]:
            with self.subTest("Test corn more food than max", answer=answer):
                [food, seed] = self.ask.corn(max, input_func=lambda: answer, try_once=True)
                self.assertTrue(food < 0 and seed < 0)
    
    @unittest.skip("Corn moved to Disrtibute class")
    def test_corn_seed_not_enough(self):
        max = 1000
        for answer in ["950 230", "950,  230", "  950 -   230.   ", "950. 230. "]:
            with self.subTest("Test corn more food than max", answer=answer):
                [food, seed] = self.ask.corn(max, input_func=lambda: answer, try_once=True)
                self.assertTrue(food == 950 and seed == 50)
    


if __name__ == "__main__":
    unittest.main()
