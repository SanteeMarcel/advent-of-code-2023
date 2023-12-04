f = open("input.txt", "r")

matrix = []

def does_number_have_gear(i_start, j_start, i_end, j_end, matrix):
    gear_indexes = set()
    for j in range(j_start, j_end + 1):
        for gear_index in has_gear_around(i_start, j, matrix):
            gear_indexes.add(gear_index)
    return gear_indexes

def has_gear_around(i, j, matrix):
    elements = [matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i + 1][j - 1], 
                matrix[i - 1][j], matrix[i + 1][j], 
                matrix[i - 1][j + 1], matrix[i][j + 1], matrix[i + 1][j + 1]]
    current_lookup_index = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, +1), (0, 1), (1, 1)]
    
    gear_indexes = []

    for ind, element in enumerate(elements):
        if element == '*' :
            gear_indexes.append(str(i + current_lookup_index[ind][0]) + ',' + str(j + current_lookup_index[ind][1]))

    return gear_indexes

for line in f:
    matrix.append(list('.' + line[:-1] + '.'))

matrix.insert(0, ['.'] * (len(line) + 1))
matrix.append(['.'] * (len(line) + 1))

indexes_and_number_dict = dict()

acc = False

for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        if element.isdigit() and not acc:
            acc = element
        elif element.isdigit() and acc:
            acc += element
        elif not element.isdigit() and acc:
            indexes_and_number_dict[str(i) + ',' + str(j - len(acc)) + ':' + str(i) + ',' + str(j - 1)] = acc
            acc = False

solution = []
gear_index_to_numbers = dict()

for key in indexes_and_number_dict.keys():
    start, end = key.split(':')
    i_start, j_start = start.split(',')
    i_end, j_end = end.split(',')
    i_start, j_start = int(i_start), int(j_start)
    i_end, j_end = int(i_end), int(j_end)

    gear_indexes = does_number_have_gear(i_start, j_start, i_end, j_end, matrix)
    
    for gear_index in gear_indexes:
        if gear_index in gear_index_to_numbers:
            gear_index_to_numbers[gear_index].append(int(indexes_and_number_dict[key]))
        else:
            gear_index_to_numbers[gear_index] = [int(indexes_and_number_dict[key])]

solution = 0

for numbers in gear_index_to_numbers.values():
    if len(numbers) == 2:
        gear_ratio = numbers[0] * numbers[1]
        solution += gear_ratio

print(solution)

f.close()
