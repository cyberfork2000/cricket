batsman = {1: {'name': 'Burns', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
           2: {'name': 'Flint', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
           3: {'name': 'Yardy', 'runs': 0, '4s': 0, "6s": 0, "balls": 0},
           4: {'name': 'Gooch', 'runs': 0, '4s': 0, "6s": 0, "balls": 0}}


def opening_batsman(openers):
    openers.pop(0)
    openers.pop(0)
    return openers


def next_batsman(batter):
    batter.pop(0)
    return batter


def batting_lineup(batting_to_come):
    lineup = []
    for i in batting_to_come.keys():
        for batter in batting_to_come[i].keys():
            if batter == 'name':
                lineup.append(batting_to_come[i]['name'])
    return lineup

batters_to_come = batting_lineup(batsman)
print(batters_to_come)
batters_to_come = opening_batsman(batters_to_come)
print(batters_to_come)

who = next_batsman(batters_to_come)

who = ' '.join(map(str, who))

print(who)


for player in batsman:
    if batsman[player]['name'] == who:
        current_batsman = batsman[player]


print("current batsman", current_batsman)


while len(batters_to_come) > 0:
    batters_to_come = next_batsman(batters_to_come)
    print(batters_to_come)
if len(batters_to_come) == 0:
    print("All Out")
else:
    print("Batsman left", len(batters_to_come))


