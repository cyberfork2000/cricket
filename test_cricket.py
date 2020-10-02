import unittest
from cricket import cricket, is_even, batsman_cross, swap_bowler


class TestCricket(unittest.TestCase):
    # def test_no_run(self):
    #     self.assertEqual(cricket(0), 'No Run')
    #
    # def test_1_run(self):
    #     self.assertEqual(cricket(1), '1 Run')
    #
    # def test_2_runs(self):
    #     self.assertEqual(cricket(2), '2 Runs')
    #
    # def test_3_runs(self):
    #     self.assertEqual(cricket(3), '3 Runs')
    #
    # def test_4_runs(self):
    #     self.assertEqual(cricket(4), 'FOUR Runs')
    #
    # def test_6_runs(self):
    #     self.assertEqual(cricket(6), 'SIX Runs')

    def test_0_runs_is_even(self):
        self.assertEqual(is_even(0), True)

    def test_2_runs_is_even(self):
        self.assertEqual(is_even(2), True)

    def test_3_runs_is_odd(self):
        self.assertEqual(is_even(3), False)

    # def test_batsman_cross(self):
    #     self.assertEqual(batsman_cross("Smith", "Jones"), "Jones")

    # def test_bowlers_swap(self):
    #     self.assertEqual(swap_bowler("Smith", "Jones"), "Jones")


if __name__ == '__main__':
    unittest.main()
