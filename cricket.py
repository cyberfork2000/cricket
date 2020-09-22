# Batman analysis = [Balls faced, 4s, 6s, SR]
# Bowler analysis = [Overs, Maidens, Runs,	Wickets, Economy]

batsman = {1: {'name': 'Burns', 'runs': 0, '4s': 0, "6s": 0},
           2: {'name': 'Flint', 'runs': 0, '4s': 0, "6s": 0}}

bowlers = {1: {'name': 'Archer', 'overs': 0, 'maidens': 0, "runs": 0},
           2: {'name': 'Broad', 'overs': 0, 'maidens': 0, "runs": 0}}

print(batsman)
print(batsman[1]['name'])
print(batsman[1]['runs'])
print(batsman[1]['4s'])
print(batsman[1]['6s'])

# def runs_scored(number):
#     if number == 0:
#         return 'No Run'
#     if number == 1:
#         return '1 Run'
#     if number == 2:
#         return '2 Runs'
#     if number == 3:
#         return '3 Runs'
#     if number == 4:
#         return 'FOUR Runs'
#     if number == 6:
#         return 'SIX Runs'


def is_even(x):
 # Define a function is_even that will take a number x as input.
    if x % 2 == 0:
        return True
    else:
        return False


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
    boundary_scored(current_batsman, runs)
    print("Bowler conceded is {}".format(current_bowler['runs']))
    print("Batsman has scored {}".format(current_batsman['runs']))


def batsman_cross(current_batsman, other_batsman):
    return other_batsman, current_batsman


def swap_bowler(current_bowler, other_bowler):
    return other_bowler, current_bowler


def new_over(current_bowler, other_bowler, current_batsman, other_batsman):
    print("NEW OVER")
    #swap bowlers & batsman
    return other_bowler, current_bowler, other_batsman, current_batsman


def end_of_over(balls_bowled_in_over, current_bowler, overs_bowled_by_bowler):
    balls_bowled_in_over += 1
    current_bowler['overs'] = str(overs_bowled_by_bowler) + "." + str(balls_bowled_in_over)
    print("Balls in over " + current_bowler['overs'])
    if balls_bowled_in_over == 6:  # end of over check
        current_bowler['overs'] = overs_bowled_by_bowler + 1
        print("END OF OVER, bowler stats are")
        print(current_bowler)
    return balls_bowled_in_over


def cricket():

    number_of_runs = None
    current_batsman = batsman[1]
    other_batsman = batsman[2]
    current_bowler = bowlers[1]
    other_bowler = bowlers[2]
    overs_bowled_by_bowler = 0
    balls_bowled_in_over = 0

    while number_of_runs != -1:
        if balls_bowled_in_over == 6:
            current_bowler, other_bowler, current_batsman, other_batsman = \
                new_over(current_bowler, other_bowler, current_batsman, other_batsman)
            balls_bowled_in_over = 0  # reset balls for over
            overs_bowled_by_bowler = current_bowler['overs']
        number_of_runs = int(input("score or -1 to end: "))
        if number_of_runs == -1:
            break
        elif is_even(number_of_runs):   # 0 2 4 6
            runs_scored_from_delivery(number_of_runs, current_batsman, current_bowler)
        elif not is_even(number_of_runs):   # 1 3
            runs_scored_from_delivery(number_of_runs, current_batsman, current_bowler)
            batting_pair_swap_ends = batsman_cross(current_batsman, other_batsman)
            current_batsman = batting_pair_swap_ends[0]
            other_batsman = batting_pair_swap_ends[1]
        balls_bowled_in_over = end_of_over(balls_bowled_in_over, current_bowler, overs_bowled_by_bowler)

    print(batsman)
    print(bowlers)


if __name__ == "__main__":
    cricket()


