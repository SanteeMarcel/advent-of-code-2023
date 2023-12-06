import re
f = open("input.txt", "r")

counter = 0

for line in f:
    counter += 1

n_of_lottos = [1] * counter

f.seek(0)

for i, line in enumerate(f):
    part1, part2 = line.split('|')

    _, part1 = part1.split(':')

    winning_numbers = set(re.findall(r'\d+', part1))
    lotto_numbers = re.findall(r'\d+', part2)

    winners = 0

    for lotto_num in lotto_numbers:
        if lotto_num in winning_numbers:
            winners += 1

    for j in range(winners):
        n_of_lottos[i + j + 1] += 1 * n_of_lottos[i]

print(sum(n_of_lottos))

f.close()
