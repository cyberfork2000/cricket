import pprint

# Batman analysis = [Balls faced, 4s, 6s, SR]
# Bowler analysis = [Overs, Maidens, Runs,	Wickets, Economy]

batsman = {1: {'name': 'Burns', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
           2: {'name': 'Flint', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
           3: {'name': 'Yardy', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
           4: {'name': 'Gooch', 'runs': 0, '4s': 0, "6s": 0, "balls": 0}}

bowlers = {1: {'name': 'Archer', 'overs': 0, 'maidens': 0, "runs": 0, "wickets": 0},
           2: {'name': 'Broad', 'overs': 0, 'maidens': 0, "runs": 0, "wickets": 0},
           3: {'name': 'Chase', 'overs': 0, 'maidens': 0, "runs": 0, "wickets": 0},
           4: {'name': 'Holder', 'overs': 0, 'maidens': 0, "runs": 0, "wickets": 0}}

# print(batsman)
# print(batsman[1]['name'])
# print(batsman[1]['runs'])
# print(batsman[1]['4s'])
# print(batsman[1]['6s'])


def is_even(x):
    return x % 2 == 0


def boundary_scored(current_batsman, runs):
    if runs == 4:
        current_batsman['4s'] = current_batsman['4s'] + 1
        print("FOUR")
    elif runs == 6:
        current_batsman['6s'] = current_batsman['6s'] + 1
        print("SIX")


def runs_scored_from_delivery(runs, current_batsman, current_bowler):
    current_bowler['runs'] = current_bowler['runs'] + runs
    current_batsman['runs'] = current_batsman['runs'] + runs
    current_batsman['balls'] = current_batsman['balls'] + 1
    boundary_scored(current_batsman, runs)
    #print("Bowler conceded is {}".format(current_bowler['runs']))
    #print("Batsman has scored {}".format(current_batsman['runs']))


def batsman_cross(current_batsman, other_batsman):
    return other_batsman, current_batsman


def swap_bowler(current_bowler, other_bowler):
    return other_bowler, current_bowler


def show_scorecard():
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
        total_wickets_taken = total_wickets_taken + bowlers[bowler]['wickets']
        pprint.pprint(bowlers[bowler]['name'] + ", "
                      + str(bowlers[bowler]['overs']) + ", "
                      + str(bowlers[bowler]['maidens']) + ", "
                      + str(bowlers[bowler]['runs']) + ", "
                      + str(bowlers[bowler]['wickets']))
    print("\n", total_runs_scored, "for", total_wickets_taken)


def new_over(current_bowler, other_bowler, current_batsman, other_batsman):
    show_scorecard()
    print("NEW OVER")
    return other_bowler, current_bowler, other_batsman, current_batsman  # swap bowlers & batsman


def latest_delivery_completed(balls_bowled_in_over):
    balls_bowled_in_over += 1
    return balls_bowled_in_over


def increment_balls_bowled_by_bowler(balls_bowled_in_over, current_bowler, overs_bowled_by_bowler):
    current_bowler['overs'] = str(overs_bowled_by_bowler) + "." + str(balls_bowled_in_over)
    print("Balls in over " + current_bowler['overs'])
    return current_bowler['overs']


def set_bowler_completed_over_count(current_bowler, overs_bowled_by_bowler):
    current_bowler['overs'] = overs_bowled_by_bowler + 1
    return current_bowler


def end_of_over_check(balls_bowled_in_over):
    if balls_bowled_in_over == 6:
        return True
    else:
        return False


def opening_batsman(openers):
    openers.pop(0)
    openers.pop(0)
    return openers


def next_batsman(batter):
    return batter.pop(0)


def batting_lineup(batting_to_come):
    lineup = []
    for i in batting_to_come.keys():
        for batter in batting_to_come[i].keys():
            if batter == 'name':
                lineup.append(batting_to_come[i]['name'])
    return lineup


def available_bowlers(who_can_bowl, current_bowler):
    eligible_bowler_list = []
    print("Available bowlers")
    for key, value in who_can_bowl.items():
        if not (value['name'] is current_bowler['name']):  # or value['name'] is other_bowler['name']
            eligible_bowler_list.append(key)
            print(str(key), value['name'])
    return eligible_bowler_list


def set_next_bowler(is_bowler_eligible):
    while True:
        try:
            choose_bowler = int(input("Choose bowler: "))
            if choose_bowler in is_bowler_eligible:
                break
            print("Invalid bowler entered")
        except Exception as e:
            print(e)
    return bowlers[choose_bowler]


def pretty(d, indent=0):  # print dictionary in pretty indenting on each key & value
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


def wicket_is_taken(the_batsman, the_bowler):
    print("OUT", the_batsman)
    runs_scored_from_delivery(0, the_batsman, the_bowler)
    return the_bowler['wickets'] + 1  # credit bowler with wicket


def next_batsman_in(batsman_in_next):
    who_is_next = next_batsman(batsman_in_next)
    for player in batsman:
        if batsman[player]['name'] == who_is_next:
            print("Next Batsman in", who_is_next)
            return batsman[player]
        else:
            return None


def enter_game_option():
    delivery_outcome = input("Enter number of runs scored (i.e. 0, 1, 2, 3, 4, 6).\nOr 'W' for wicket.\nOr 'Q' to "
                             "quit\n>> ")
    return delivery_outcome.upper()


def choose_new_bowler(current_bowler):
    bowler_list = available_bowlers(bowlers, current_bowler)
    return set_next_bowler(bowler_list)  # return set_next_bowler(bowler_list)


def display_bowler_end_of_over_stats(current_bowler):
    print("END OF OVER, bowler stats are")
    print(current_bowler)


def change_bowler_for_next_over(current_bowler):
    if input("Change bowler? ") is 'y':
        return choose_new_bowler(current_bowler)
    else:
        print("no change")


def cricket():
    delivery_outcome = None
    batters_to_come = batting_lineup(batsman)
    print("Complete batting lineup is", batters_to_come)
    current_batsman = batsman[1]
    other_batsman = batsman[2]
    batters_to_come = opening_batsman(batters_to_come)
    print("Batters following the openers", batters_to_come)
    current_bowler = bowlers[1]
    other_bowler = bowlers[2]
    overs_bowled_by_bowler = 0
    balls_bowled_in_over = 0
    end_of_innings = False
    last_ball_of_over = False

    while delivery_outcome != "Q" and end_of_innings is False:
        if last_ball_of_over is True:
            current_bowler = set_bowler_completed_over_count(current_bowler, overs_bowled_by_bowler)
            display_bowler_end_of_over_stats(current_bowler)

            if input("Change bowler? ") is 'y':
                bowler_list = available_bowlers(bowlers, current_bowler)
                other_bowler = set_next_bowler(bowler_list)
####
#            other_bowler = change_bowler_for_next_over(current_bowler)
####
            balls_bowled_in_over = 0  # reset balls for over
            last_ball_of_over = False
            current_bowler, other_bowler, current_batsman, other_batsman = \
                new_over(current_bowler, other_bowler, current_batsman, other_batsman)
            overs_bowled_by_bowler = current_bowler['overs']

        delivery_outcome = enter_game_option()
        if delivery_outcome[0] == "W":
            current_bowler['wickets'] = wicket_is_taken(current_batsman, current_bowler)
            # next batsman in
            if len(batters_to_come) > 0:
                current_batsman = next_batsman_in(batters_to_come)
            elif len(batters_to_come) == 0:
                print("All Out")
                end_of_innings = True
        elif delivery_outcome.isnumeric():
            delivery_outcome = int(delivery_outcome)
            if is_even(delivery_outcome):  # 0 2 4 6
                runs_scored_from_delivery(delivery_outcome, current_batsman, current_bowler)
            elif not is_even(delivery_outcome):  # 1 3
                runs_scored_from_delivery(delivery_outcome, current_batsman, current_bowler)
                current_batsman, other_batsman = batsman_cross(current_batsman, other_batsman)
        elif delivery_outcome[0] == "Q":
            print("End of match!")
            break
        balls_bowled_in_over = latest_delivery_completed(balls_bowled_in_over)
        current_bowler['overs'] = increment_balls_bowled_by_bowler(
            balls_bowled_in_over, current_bowler, overs_bowled_by_bowler)
        last_ball_of_over = end_of_over_check(balls_bowled_in_over)

    show_scorecard()


if __name__ == "__main__":
    cricket()
