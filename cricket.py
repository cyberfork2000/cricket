import pprint


def action_during_innings(innings):
    delivery_outcome = None
    last_ball_of_over = False
    end_of_innings = False

    while delivery_outcome != "Q" and end_of_innings is False:
        if last_ball_of_over is True:
            innings.current_bowler = \
                innings.set_bowler_completed_over_count(innings.current_bowler, innings.overs_bowled_by_bowler)
            innings.display_bowler_end_of_over_stats(innings.current_bowler)
            innings.show_scorecard(innings.batsman, innings.bowlers)
            if input("Change bowler? ") is 'y':
                innings.bowler_list = \
                    innings.available_bowlers(innings.bowlers, innings.current_bowler)
                innings.other_bowler = \
                    innings.set_next_bowler(innings.bowler_list, innings.bowlers)
            innings.balls_bowled_in_over = 0  # reset balls for over
            innings.current_bowler, innings.other_bowler, \
                innings.current_batsman, innings.other_batsman = innings.new_over(
                    innings.current_bowler, innings.other_bowler,
                    innings.current_batsman, innings.other_batsman)
            innings.overs_bowled_by_bowler = innings.current_bowler['overs']

        delivery_outcome = innings.enter_game_option()
        if delivery_outcome[0] == "W":
            innings.current_bowler['wickets'] = innings.wicket_is_taken(innings.current_batsman, innings.current_bowler)
            # next batsman in
            if len(innings.the_batting_order) > 0:
                innings.current_batsman = innings.next_batsman_in_after_fall_of_wicket(innings)

            elif len(innings.the_batting_order) == 0:
                print("All Out")
                end_of_innings = True
        elif delivery_outcome.isnumeric():
            delivery_outcome = int(delivery_outcome)
            if innings.is_even(delivery_outcome):  # 0 2 4 6
                innings.runs_scored_from_delivery(delivery_outcome, innings.current_batsman, innings.current_bowler)
            elif not innings.is_even(delivery_outcome):  # 1 3
                innings.runs_scored_from_delivery(delivery_outcome, innings.current_batsman, innings.current_bowler)
                innings.current_batsman, innings.other_batsman = innings.batsman_cross(
                    innings.current_batsman,
                    innings.other_batsman)
        elif delivery_outcome[0] == "Q":
            print("End of match!")
            break
        innings.balls_bowled_in_over = innings.latest_delivery_completed(innings.balls_bowled_in_over)
        innings.current_bowler['overs'] = innings.increment_balls_bowled_by_bowler(
            innings.balls_bowled_in_over, innings.current_bowler, innings.overs_bowled_by_bowler)
        last_ball_of_over = innings.end_of_over_check(innings.balls_bowled_in_over)

    #return innings.batsman, innings.bowlers


class Cricket(object):

    def __init__(self):

        self.batsman = {1: {'name': 'Burns', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
                        2: {'name': 'Flint', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
                        3: {'name': 'Yards', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
                        4: {'name': 'Hooch', 'runs': 0, '4s': 0, "6s": 0, "balls": 0}}

        self.bowlers = {1: {'name': 'Archer', 'overs': 0, 'maidens': 0, "runs": 0, "wickets": 0},
                        2: {'name': 'Broad', 'overs': 0, 'maidens': 0, "runs": 0, "wickets": 0},
                        3: {'name': 'Chase', 'overs': 0, 'maidens': 0, "runs": 0, "wickets": 0},
                        4: {'name': 'Holder', 'overs': 0, 'maidens': 0, "runs": 0, "wickets": 0}}

        self.the_batting_order = self.batting_lineup(self.batsman)
        print("Complete batting lineup is", self.the_batting_order)
        self.current_batsman = self.batsman[1]
        self.other_batsman = self.batsman[2]
        self.the_batting_order = self.opening_batsman(self.the_batting_order)
        print("Batters following the openers", self.the_batting_order)
        self.current_bowler = self.bowlers[1]
        self.other_bowler = self.bowlers[2]
        self.overs_bowled_by_bowler = 0
        self.balls_bowled_in_over = 0

    @staticmethod
    def is_even(x):
        return x % 2 == 0

    def boundary_scored(self, runs):
        if runs == 4:
            self.current_batsman['4s'] = self.current_batsman['4s'] + 1
            print("FOUR")
        elif runs == 6:
            self.current_batsman['6s'] = self.current_batsman['6s'] + 1
            print("SIX")

    def runs_scored_from_delivery(self, runs, the_current_batsman, the_current_bowler):
        the_current_bowler['runs'] = the_current_bowler['runs'] + runs
        the_current_batsman['runs'] = the_current_batsman['runs'] + runs
        the_current_batsman['balls'] = the_current_batsman['balls'] + 1
        self.boundary_scored(runs)

    @staticmethod
    def batsman_cross(the_current_batsman, the_other_batsman):
        return the_other_batsman, the_current_batsman

    @staticmethod
    def swap_bowler(the_current_bowler, the_other_bowler):
        return the_other_bowler, the_current_bowler

    @staticmethod
    def show_scorecard(batsman, bowlers):
        print("Scorecard")
        total_runs_scored = 0
        print("Batsman / Runs / 4s / 6s / Balls")
        for batter in batsman:
            total_runs_scored = total_runs_scored + batsman[batter]['runs']
            pprint.pprint(batsman[batter]['name'] + ", "
                          + str(batsman[batter]['runs']) + ", "
                          + str(batsman[batter]['4s']) + ", "
                          + str(batsman[batter]['6s']) + ", "
                          + str(batsman[batter]['balls']))
        print("===================================")
        total_wickets_taken = 0
        print("Bowler / Overs / Maidens / Runs / Wickets")
        for bowler in bowlers:
            if float(bowlers[bowler]['overs']) > 0:
                total_wickets_taken = total_wickets_taken + bowlers[bowler]['wickets']
                pprint.pprint(bowlers[bowler]['name'] + ", "
                              + str(bowlers[bowler]['overs']) + ", "
                              + str(bowlers[bowler]['maidens']) + ", "
                              + str(bowlers[bowler]['runs']) + ", "
                              + str(bowlers[bowler]['wickets']))
        print("\n", total_runs_scored, "for", total_wickets_taken)

    @staticmethod
    def new_over(the_current_bowler, the_other_bowler, the_current_batsman, the_other_batsman):
        return the_other_bowler, the_current_bowler, the_other_batsman, the_current_batsman  # swap bowlers & batsman

    @staticmethod
    def latest_delivery_completed(the_balls_bowled_in_over):
        the_balls_bowled_in_over += 1
        return the_balls_bowled_in_over

    @staticmethod
    def increment_balls_bowled_by_bowler(the_balls_bowled_in_over, the_current_bowler, the_overs_bowled_by_bowler):
        the_current_bowler['overs'] = str(the_overs_bowled_by_bowler) + "." + str(the_balls_bowled_in_over)
        print("Balls in over " + the_current_bowler['overs'])
        return the_current_bowler['overs']

    @staticmethod
    def set_bowler_completed_over_count(the_current_bowler, the_overs_bowled_by_bowler):
        the_current_bowler['overs'] = the_overs_bowled_by_bowler + 1
        return the_current_bowler

    @staticmethod
    def end_of_over_check(the_balls_bowled_in_over):
        if the_balls_bowled_in_over == 6:
            return True
        else:
            return False

    @staticmethod
    def opening_batsman(openers):
        openers.pop(0)
        openers.pop(0)
        return openers

    @staticmethod
    def batting_lineup(batting_to_come):
        lineup = []
        for i in batting_to_come.keys():
            for batter in batting_to_come[i].keys():
                if batter == 'name':
                    lineup.append(batting_to_come[i]['name'])
        return lineup

    @staticmethod
    def available_bowlers(who_can_bowl, the_current_bowler):
        eligible_bowler_list = []
        print("Available bowlers")
        for key, value in who_can_bowl.items():
            if not (value['name'] is the_current_bowler['name']):  # or value['name'] is other_bowler['name']
                eligible_bowler_list.append(key)
                print(str(key), value['name'])
        return eligible_bowler_list

    @staticmethod
    def set_next_bowler(is_bowler_eligible, bowlers):
        while True:
            try:
                choose_bowler = int(input("Choose bowler: "))
                if choose_bowler in is_bowler_eligible:
                    break
                print("Invalid bowler entered")
            except Exception as e:
                print(e)
        return bowlers[choose_bowler]

    def wicket_is_taken(self, the_batsman, the_bowler):
        print("OUT", the_batsman)
        self.runs_scored_from_delivery(0, the_batsman, the_bowler)
        return the_bowler['wickets'] + 1  # credit bowler with wicket

    @staticmethod
    def enter_game_option():
        the_delivery_outcome = input("Enter number of runs scored (i.e. 0, 1, 2, 3, 4, 6)."
                                     "\nOr 'W' for wicket."
                                     "\nOr 'Q' to quit. ")
        return the_delivery_outcome.upper()

    def choose_new_bowler(self, the_current_bowler):
        the_bowler_list = self.available_bowlers(self.bowlers, the_current_bowler)
        return self.set_next_bowler(the_bowler_list, self.bowlers)

    @staticmethod
    def display_bowler_end_of_over_stats(the_current_bowler):
        print("END OF OVER, bowler stats are\n", the_current_bowler)

    def change_bowler_for_next_over(self, the_current_bowler):
        if input("Change bowler? ") is 'y':
            return self.choose_new_bowler(the_current_bowler)
        else:
            print("no change")

    def next_batsman_in_after_fall_of_wicket(self, innings):
        next_man_in = self.the_batting_order.pop(0)

        for key, player in innings.batsman.items():
            if next_man_in == player['name']:
                self.current_batsman = player

        print("Next Batsman in", self.current_batsman)
        return self.current_batsman


if __name__ == '__main__':
    FirstInnings = Cricket()
    action_during_innings(FirstInnings)
    FirstInnings.show_scorecard(FirstInnings.batsman, FirstInnings.bowlers)
    ########################
    SecondInnings = Cricket()
    action_during_innings(SecondInnings)
    SecondInnings.show_scorecard(SecondInnings.batsman, SecondInnings.bowlers)