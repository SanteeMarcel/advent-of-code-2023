f = open("input.txt", "r")

matrix = []

def does_number_have_symbol(i_start, j_start, j_end, matrix):
    for j in range(j_start, j_end + 1):
        if has_symbol_around(i_start, j, matrix):
            return True
    
    return False

def has_symbol_around(i, j, matrix):
    elements = [matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i + 1][j - 1], 
                matrix[i - 1][j], matrix[i + 1][j], 
                matrix[i - 1][j + 1], matrix[i][j + 1], matrix[i + 1][j + 1]]
    
    for element in elements:
        if element != '.' and not element.isdigit():
            return True

    return False

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

for key in indexes_and_number_dict.keys():
    start, end = key.split(':')
    i_start, j_start = start.split(',')
    i_end, j_end = end.split(',')
    i_start, j_start = int(i_start), int(j_start)
    i_end, j_end = int(i_end), int(j_end)
    if does_number_have_symbol(i_start, j_start, j_end, matrix):
        solution.append(int(indexes_and_number_dict[key]))

print(sum(solution))

f.close()
