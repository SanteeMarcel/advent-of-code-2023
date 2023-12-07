from math import sqrt, floor, ceil

f = open("input.txt", "r")

time = int(''.join(filter(str.isdigit, f.readline())))
distance = int(''.join(filter(str.isdigit, f.readline())))

solution = None

    # total_distance > (MAX_TIME - pressing_time)*pressing_time
pressing_time_higher = (time + sqrt((time ** 2) - 4*distance)) / 2
pressing_time_lower = (time - sqrt((time ** 2) - 4*distance)) / 2
if int(pressing_time_higher) == pressing_time_higher:
    pressing_time_higher -= 1
if int(pressing_time_lower) == pressing_time_lower:
    pressing_time_lower += 1
solution = floor(pressing_time_higher) - ceil(pressing_time_lower) + 1

print(solution)

f.close()
