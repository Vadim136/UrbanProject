import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        wlkr = runner.Runner("walker")
        i = 0
        while i <= 9:
            i+=1
            wlkr.walk()
            
        self.assertEqual(wlkr.distance, 50)
        
    def test_run(self):
        rnnr = runner.Runner("runner")
        i = 0
        while i <= 9:
            i+=1
            rnnr.run()
            
        self.assertEqual(rnnr.distance, 100)
        
    def test_challenge(self):
        wlkr = runner.Runner("walker")
        rnnr = runner.Runner("runner")
        i = 0
        while i <= 9:
            i+=1
            wlkr.walk()
            rnnr.run()
            
        self.assertNotEqual(wlkr.distance, rnnr.distance)
        
        
        
if __name__=="__main__":
    unittest.main()