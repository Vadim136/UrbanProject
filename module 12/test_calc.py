import calc
import unittest
import random

# def test_add():
    
#     if calc.add( 1, 2) == 3:
        
#         print("Test add(a,b) is 0K")
#     else:
#         print("Test add(a,b) is fail")
# test_add()


class CalcTest(unittest.TestCase):
    
    def tearDown(self):
        # return super().tearDown()
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    
    
    @unittest.skip("Проверка skip")
    def test_add(self):
        self.assertEqual(calc.add(1,2), 3)
        
    @unittest.skipIf(random.randint(0, 2), "Тест skipIf")
    def test_sub(self):
        self.assertEqual(calc.sub(5,3), 2)
        
    def test_mul(self):
        self.assertEqual (calc.mul(2, 5), 10)
        
    def test_div(self):
        self.assertEqual (calc.div(8, 4), 2)
        
        
if __name__=="__main__":
    unittest.main()