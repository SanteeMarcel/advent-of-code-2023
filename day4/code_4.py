from math import floor
import re
f = open("input.txt", "r")

t_winners = 0

for line in f:
    part1, part2 = line.split('|')

    _, part1 = part1.split(':')

    winning_numbers = set(re.findall(r'\d+', part1))
    lotto_numbers = re.findall(r'\d+', part2)

    winners = 0

    for lotto_num in lotto_numbers:
        if lotto_num in winning_numbers:
            winners += 1
    t_winners += floor(2 ** (winners - 1)) 

print(t_winners)

f.close()
