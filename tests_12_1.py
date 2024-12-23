import unittest
from module_12.runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        v = Runner('Vladimir')
        for w in range(1, 11):
            v.walk()
        self.assertEqual(v.distance, 50)

    def test_run(self):
        i = Runner('Ivan')
        for r in range(1, 11):
            i.run()
        self.assertEqual(i.distance, 100)

    def test_challenge(self):
        v = Runner('Vladimir')
        i = Runner('Ivan')
        for w in range(1, 11):
            v.walk()
        for r in range(1, 11):
            i.run()
        self.assertNotEqual(v.distance, i.distance)


if __name__ == '__main__':
    unittest.main()
