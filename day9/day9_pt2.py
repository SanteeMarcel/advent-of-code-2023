f = open("input.txt", "r")

def is_geometric_sequence(sequence):
    if len(sequence) < 2:
        return False 
    
    if sequence[0] == 0:
        return False

    ratio = sequence[1] / sequence[0]

    for i in range(1, len(sequence) - 1):
        if sequence[i] == 0:
            return False
        if sequence[i + 1] / sequence[i] != ratio:
            return False

    return ratio

def is_arithmetic_sequence(sequence):
    if len(sequence) < 2:
        return False

    difference = sequence[1] - sequence[0]

    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != difference:
            return False

    return difference


def get_prev_number(sequence):
    if is_geometric_sequence(sequence):
        return sequence[0]/is_geometric_sequence(sequence)
    if is_arithmetic_sequence(sequence):
        return  sequence[0] - is_arithmetic_sequence(sequence) 
    if len(set(sequence)) == 1:
        return sequence[0]
    new_sequence = []
    for i in range(len(sequence) - 1):
        new_sequence.append(sequence[i + 1] - sequence[i])
    return sequence[0] - get_prev_number(new_sequence)
   

sequences = []

for line in f.readlines():
    sequences.append(list(map(lambda x : int(x), line.split())))

solution = []

for sequence in sequences:
    solution.append(
        get_prev_number(sequence)
    )

print(solution)
print(sum(solution))

f.close()
