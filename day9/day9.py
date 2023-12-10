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


def get_next_number(sequence):
    if is_geometric_sequence(sequence):
        return is_geometric_sequence(sequence)*sequence[-1]
    if is_arithmetic_sequence(sequence):
        return is_arithmetic_sequence(sequence) + sequence[-1] 
    if len(set(sequence)) == 1:
        return sequence[0]
    new_sequence = []
    for i in range(len(sequence) - 1):
        new_sequence.append(sequence[i + 1] - sequence[i])
    return sequence[-1] + get_next_number(new_sequence)
   

sequences = []

for line in f.readlines():
    sequences.append(list(map(lambda x : int(x), line.split())))

solution = []

for sequence in sequences:
    solution.append(
        get_next_number(sequence)
    )

print(solution)
print(sum(solution))

f.close()
