import logging
import unittest

from module_12.rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            self.runner1 = Runner('Усэйн', -10)
            for w in range(1, 11):
                self.runner1.walk()
            self.assertEqual(self.runner1.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.runner2 = Runner(12345, 9)
            for r in range(1, 11):
                self.runner2.run()
            self.assertEqual(self.runner2.distance, 180)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        for w in range(1, 11):
            self.runner1.walk()
        for r in range(1, 11):
            self.runner2.run()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)


if __name__ == '__main__':
    unittest.main()
