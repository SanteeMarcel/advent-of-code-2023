from collections import Counter

kind_to_power_map = { 'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0 }
type_to_power_map = { 'Five of a kind':6 , 'Four of a kind': 5, 'Full house': 4, 'Three of a kind': 3, 'Two pair': 2, 'One pair': 1, 'High card': 0 }

f = open("input.txt", "r")

power_arr = []
hand_arr = []
index = 0
bid_arr = []
aaaa = []

for line in f.readlines():
    hand, bid = line.split(' ')
    bid = int(bid)
    bid_arr.append(bid)
    hand = hand.split(' ')[0]
    aaaa.append(hand)
    numeric_hand = [-1]*5
    for i, card in enumerate(hand):
        numeric_hand[i] = kind_to_power_map[card]
    hand_arr.append(numeric_hand)

    count_hand = Counter(hand)
    values = list(count_hand.values())

    if len(values) == 1:
        power_arr.append(type_to_power_map['Five of a kind'])
    elif len(values) == 2 and ( (values[0] == 4 and values[1] == 1) or (values[0] == 1 and values[1] == 4) ):
        power_arr.append(type_to_power_map['Four of a kind'])
    elif len(values) == 2:
        power_arr.append(type_to_power_map['Full house'])
    elif len(values) == 3 and any(x == 3 for x in values):
        power_arr.append(type_to_power_map['Three of a kind'])
    elif len(values) == 3:
        power_arr.append(type_to_power_map['Two pair'])
    elif len(values) == 4:
        power_arr.append(type_to_power_map['One pair'])
    elif len(values) == 5:
        power_arr.append(type_to_power_map['High card'])

index_power_hand_tuples = list(zip([i for i in range(len(power_arr))], power_arr, hand_arr, aaaa))

index_power_hand_tuples = sorted(index_power_hand_tuples, key= lambda x : (x[1], x[2]))

solution = 0

for rank, index_power_hand_tuple in enumerate(index_power_hand_tuples):
    solution += (rank + 1) * bid_arr[index_power_hand_tuple[0]]

print(solution)

f.close()
