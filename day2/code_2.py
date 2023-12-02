import re

f = open("input.txt", "r")

possible_games_counter = 0

# only 12 red cubes, 13 green cubes, and 14 blue cubes?

limits = { 'r' : 12,'g' :13, 'b' : 14 }

def is_valid_game(game):
    for mset in game:
        mlist = re.findall(r'\d+\s[rgb]', mset)
        for color in mlist:
            color = color.split(' ')
            if int(color[0]) > limits[color[-1]]:
                return False
    
    return True

index = 0

for game in f:
    index += 1
    game = game.split(';')

    if not is_valid_game(game):
        continue

    possible_games_counter += index


print(possible_games_counter)

f.close()
