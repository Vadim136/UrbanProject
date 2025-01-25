import unittest

# Предположим, что классы Runner и Tournament уже определены в модуле my_module
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(cls.all_results[key])

    @unittest.skipIf( is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.__class__.all_results[0] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf( is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.__class__.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf( is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

        
if __name__ == '__main__':
    unittest.main()
