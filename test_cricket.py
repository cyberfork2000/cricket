import unittest
from cricket import Cricket


class TestCricket(unittest.TestCase):

    def test_0_runs_is_even(self):
        self.assertEqual(Cricket.is_even(0), True)

    def test_2_runs_is_even(self):
        self.assertEqual(Cricket.is_even(2), True)

    def test_3_runs_is_odd(self):
        self.assertEqual(Cricket.is_even(3), False)

    def test_batsman_cross(self):
        self.assertEqual(Cricket.batsman_cross("Smith", "Jones"), ("Jones", "Smith"))

    def test_bowlers_swap(self):
        self.assertEqual(Cricket.swap_bowler("Smith", "Jones"), ("Jones", "Smith"))

    def test_new_over(self):
        self.assertEqual(Cricket.new_over("Archer", "Baker", "Charles", "Draper"), ("Baker", "Archer", "Draper", "Charles"))

    def test_zero_balls_bowled(self):
        self.assertEqual(Cricket.end_of_over_check(0), False)

    def test_second_ball_bowled(self):
        self.assertEqual(Cricket.end_of_over_check(2), False)

    def test_sixth_ball_bowled(self):
        self.assertEqual(Cricket.end_of_over_check(6), True)

    def test_first_delivery_of_over_completed(self):
        self.assertEqual(Cricket.latest_delivery_completed(0), 1)

    def test_second_delivery_of_over_completed(self):
        self.assertEqual(Cricket.latest_delivery_completed(1), 2)

    def test_sixth_delivery_of_over_completed(self):
        self.assertEqual(Cricket.latest_delivery_completed(5), 6)

    def test_first_ball_in_over_count(self):
        self.assertEqual(Cricket.increment_balls_bowled_by_bowler(1, {'overs': 0}, 0), "0.1")

    def test_second_ball_in_over_count(self):
        self.assertEqual(Cricket.increment_balls_bowled_by_bowler(2, {'overs': 0}, 0), "0.2")

    def test_sixth_ball_in_over_count(self):
        self.assertEqual(Cricket.increment_balls_bowled_by_bowler(6, {'overs': 0}, 0), "0.6")

    def test_first_ball_in_second_over_count(self):
        self.assertEqual(Cricket.increment_balls_bowled_by_bowler(1, {'overs': 1}, 1), "1.1")

    def test_fifth_ball_in_second_over_count(self):
        self.assertEqual(Cricket.increment_balls_bowled_by_bowler(5, {'overs': 1}, 1), "1.5")

    def test_bowler_completes_first_over(self):
        self.assertEqual(Cricket.set_bowler_completed_over_count(
            {'name': 'Archer', 'overs': 0, 'maidens': 0, 'runs': 0, 'wickets': 0}, 0),
            {'name': 'Archer', 'overs': 1, 'maidens': 0, 'runs': 0, 'wickets': 0})

    def test_bowler_completes_second_over(self):
        self.assertEqual(Cricket.set_bowler_completed_over_count(
            {'name': 'Archer', 'overs': 1, 'maidens': 0, 'runs': 0, 'wickets': 0}, 1),
            {'name': 'Archer', 'overs': 2, 'maidens': 0, 'runs': 0, 'wickets': 0})


if __name__ == '__main__':
    unittest.main()
