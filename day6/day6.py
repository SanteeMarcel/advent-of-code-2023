from math import sqrt, floor, ceil
import numpy as np

f = open("input.txt", "r")

times = list(map(int, filter(lambda x: x.isdigit(), f.readline().split('\n')[0].split(' '))))
distances = list(map(int, filter(lambda x: x.isdigit(), f.readline().split('\n')[0].split(' '))))

solutions = [1]*len(times)

for i, td_tuple in enumerate(zip(times, distances)):
    time, distance = td_tuple
    # total_distance > (MAX_TIME - pressing_time)*pressing_time
    pressing_time_higher = (time + sqrt((time ** 2) - 4*distance)) / 2
    pressing_time_lower = (time - sqrt((time ** 2) - 4*distance)) / 2
    if int(pressing_time_higher) == pressing_time_higher:
        pressing_time_higher -= 1
    if int(pressing_time_lower) == pressing_time_lower:
        pressing_time_lower += 1
    solutions[i] = floor(pressing_time_higher) - ceil(pressing_time_lower) + 1

print(np.prod(solutions))

f.close()
