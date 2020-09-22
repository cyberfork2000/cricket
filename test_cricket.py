import unittest
from cricket import cricket


class TestCricket(unittest.TestCase):
    def test_no_run(self):
        self.assertEqual(cricket(0), 'No Run')

    def test_1_run(self):
        self.assertEqual(cricket(1), '1 Run')

    def test_2_runs(self):
        self.assertEqual(cricket(2), '2 Runs')

    def test_3_runs(self):
        self.assertEqual(cricket(3), '3 Runs')

    def test_4_runs(self):
        self.assertEqual(cricket(4), 'FOUR Runs')

    def test_6_runs(self):
        self.assertEqual(cricket(6), 'SIX Runs')


if __name__ == '__main__':
    unittest.main()
