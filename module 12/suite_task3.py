import unittest
import tast_runner, test_runner2

runST = unittest.TestSuite()

runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tast_runner.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(runST)