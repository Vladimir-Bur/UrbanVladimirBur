import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

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

    def testTournament_1(self):
        self.ttn1 = Tournament(90, self.runner1, self.runner2)
        ttn1_test = self.ttn1.start()
        TournamentTest.all_results.append({r: str(ttn1_test[r]) for r in range(1, len(ttn1_test) + 1)})
        self.assertTrue(TournamentTest.all_results[0][2] == self.runner2.name)

    def testTournament_2(self):
        self.ttn2 = Tournament(90, self.runner2, self.runner3)
        ttn2_test = self.ttn2.start()
        TournamentTest.all_results.append({r: str(ttn2_test[r]) for r in range(1, len(ttn2_test) + 1)})
        self.assertTrue(TournamentTest.all_results[1][2] == self.runner3.name)

    def testTournament_3(self):
        self.ttn3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        ttn3_test = self.ttn3.start()
        TournamentTest.all_results.append({r: str(ttn3_test[r]) for r in range(1, len(ttn3_test) + 1)})
        self.assertTrue(TournamentTest.all_results[2][3] == self.runner3.name)

if __name__ == '__main__':
    unittest.main()
