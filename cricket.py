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


def end_of_over(balls_bowled_in_over, current_bowler, overs_bowled_by_bowler):
    balls_bowled_in_over += 1
    current_bowler['overs'] = str(overs_bowled_by_bowler) + "." + str(balls_bowled_in_over)
    print("Balls in over " + current_bowler['overs'])
    if balls_bowled_in_over == 6:  # end of over check
        current_bowler['overs'] = overs_bowled_by_bowler + 1
        print("END OF OVER, bowler stats are")
        print(current_bowler)
    return balls_bowled_in_over


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


def available_bowlers(who_can_bowl, current_bowler, other_bowler):
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


def cricket():
    number_of_runs = None
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

    while number_of_runs != -1 and end_of_innings is False:
        if balls_bowled_in_over == 6:
            if input("Change bowler? ") is 'y':
                bowler_list = available_bowlers(bowlers, current_bowler, other_bowler)
                current_bowler = set_next_bowler(bowler_list)
            else:
                current_bowler, other_bowler, current_batsman, other_batsman = \
                    new_over(current_bowler, other_bowler, current_batsman, other_batsman)
            balls_bowled_in_over = 0  # reset balls for over
            overs_bowled_by_bowler = current_bowler['overs']
        number_of_runs = int(input("score or -1 to end: "))
        if number_of_runs == -1:
            print("End of match!")
            break
        elif number_of_runs == -2:
            print("wicket")
            runs_scored_from_delivery(0, current_batsman, current_bowler)
            current_bowler['wickets'] = current_bowler['wickets'] + 1  # credit bowler with wicket
            # next batsman in
            print("OUT", current_batsman)
            number_of_batsman_left = len(batters_to_come)
            if number_of_batsman_left > 0:
                who_is_next = next_batsman(batters_to_come)
                for i in batsman:
                    if batsman[i]['name'] == who_is_next:
                        print("Next Batsman in", who_is_next)
                        current_batsman = batsman[i]
                        break
            elif number_of_batsman_left == 0:
                print("All Out")
                end_of_innings = True
        elif is_even(number_of_runs):  # 0 2 4 6
            runs_scored_from_delivery(number_of_runs, current_batsman, current_bowler)
        elif not is_even(number_of_runs):  # 1 3
            runs_scored_from_delivery(number_of_runs, current_batsman, current_bowler)
            current_batsman, other_batsman = batsman_cross(current_batsman, other_batsman)
        balls_bowled_in_over = end_of_over(balls_bowled_in_over, current_bowler, overs_bowled_by_bowler)

    show_scorecard()


if __name__ == "__main__":
    cricket()
