import unittest
from module_12.runner import Runner
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        v = Runner('Vladimir')
        for w in range(1, 11):
            v.walk()
        self.assertEqual(v.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        i = Runner('Ivan')
        for r in range(1, 11):
            i.run()
        self.assertEqual(i.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        v = Runner('Vladimir')
        i = Runner('Ivan')
        for w in range(1, 11):
            v.walk()
        for r in range(1, 11):
            i.run()
        self.assertNotEqual(v.distance, i.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for kv in TournamentTest.all_results:
            print(kv)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def testTournament_1(self):
        self.ttn1 = Tournament(90, self.runner1, self.runner2)
        ttn1_test = self.ttn1.start()
        TournamentTest.all_results.append({r: str(ttn1_test[r]) for r in range(1, len(ttn1_test) + 1)})
        self.assertTrue(TournamentTest.all_results[0][2] == self.runner2.name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def testTournament_2(self):
        self.ttn2 = Tournament(90, self.runner2, self.runner3)
        ttn2_test = self.ttn2.start()
        TournamentTest.all_results.append({r: str(ttn2_test[r]) for r in range(1, len(ttn2_test) + 1)})
        self.assertTrue(TournamentTest.all_results[1][2] == self.runner3.name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def testTournament_3(self):
        self.ttn3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        ttn3_test = self.ttn3.start()
        TournamentTest.all_results.append({r: str(ttn3_test[r]) for r in range(1, len(ttn3_test) + 1)})
        self.assertTrue(TournamentTest.all_results[2][3] == self.runner3.name)

if __name__ == '__main__':
    unittest.main()