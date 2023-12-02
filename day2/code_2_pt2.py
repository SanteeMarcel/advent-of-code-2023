import re

f = open("input.txt", "r")

def max_tuple(game):
    max_r, max_g, max_b = 0, 0, 0
    for mset in game:
        mlist = re.findall(r'\d+\s[rgb]', mset)
        for color in mlist:
            color = color.split(' ')
            if color[-1] == 'r':
                max_r = max(max_r, int(color[0]))
            if color[-1] == 'g':
                max_g = max(max_g, int(color[0]))
            if color[-1] == 'b':
                max_b = max(max_b, int(color[0]))
    return (max_r, max_g, max_b)

counter = 0

for game in f:
    game = game.split(';')

    r, g, b = max_tuple(game)
    print(r,g, b)
    counter += r*g*b


print(counter)

f.close()
