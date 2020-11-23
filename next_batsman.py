batsman = {1: {'name': 'Burns', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
           2: {'name': 'Flint', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
           3: {'name': 'Yardy', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
           4: {'name': 'Gooch', 'runs': 0, '4s': 0, "6s": 0, "balls": 0}}


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


batters_to_come = batting_lineup(batsman)
print("Complete batting lineup is", batters_to_come)
# print(len(batters_to_come))
# batters_to_come = opening_batsman(batters_to_come)
# print(len(batters_to_come))
# print(batters_to_come)
#
# print(len(batters_to_come))
# next_man = next_batsman(batters_to_come)
# print(len(batters_to_come))
# print(next_man)
# print(batters_to_come)
#
# for player in batsman:
#     if batsman[player]['name'] == next_man:
#         current_batsman = batsman[player]
#
#
# print("current batsman", current_batsman)


while len(batters_to_come) > 0:
    who_is_next = next_batsman(batters_to_come)
    print("Next batsman is", who_is_next)
    print("Remaining batsman are", batters_to_come)

if len(batters_to_come) == 0:
    print("All Out")
# else:
#     print("Batsman left", len(batters_to_come))


