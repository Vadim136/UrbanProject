import unittest
import test_calc, new_test_calc


calcST = unittest.TestSuite()

calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calc.CalcTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(new_test_calc.NewCalcTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(calcST)