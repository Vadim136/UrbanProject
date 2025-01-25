import logging
import rt_with_exceptions
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            wlkr = rt_with_exceptions.Runner("walker1", speed=-5)  # Passing negative speed
            i = 0
            while i <= 9:
                i += 1
                wlkr.walk()

            self.assertEqual(wlkr.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            rnnr = rt_with_exceptions.Runner(123, 10)  # Passing non-string name
            i = 0
            while i <= 9:
                i += 1
                rnnr.run()

            self.assertEqual(rnnr.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        wlkr = rt_with_exceptions.Runner("walker2", 5)
        rnnr = rt_with_exceptions.Runner("runner2", 10)
        i = 0
        while i <= 9:
            i += 1
            wlkr.walk()
            rnnr.run()

        self.assertNotEqual(wlkr.distance, rnnr.distance)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                        format="%(asctime)s | %(levelname)s | %(message)s", encoding="UTF-8")
    unittest.main()
