from re import findall
from math import lcm

f = open("input.txt", "r")

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

instructions = f.readline()[:-1]
f.readline()

value_to_node_map = dict()

for line in f.readlines():
    curr_location, destination = line.split('=')
    curr_location = curr_location[:-1]

    left_destination, right_destination = destination.split(',')
    right_destination = ''.join(findall(r'[0-9]|[A-Z]',  right_destination))
    left_destination =  ''.join(findall(r'[0-9]|[A-Z]',  left_destination))

    if curr_location in value_to_node_map:
        current_node = value_to_node_map[curr_location]
    else:
        current_node = Node(curr_location)
        value_to_node_map[curr_location] = current_node

    if left_destination in value_to_node_map:
        current_node.left = value_to_node_map[left_destination]
    else:
        current_node.left = Node(left_destination)
        value_to_node_map[left_destination] = current_node.left

    if right_destination in value_to_node_map:
        current_node.right = value_to_node_map[right_destination]
    else:
        current_node.right = Node(right_destination)
        value_to_node_map[right_destination] = current_node.right


starting_locations = list(filter(lambda x : x[-1] == 'A', value_to_node_map.keys()))

pointer_nodes = [value_to_node_map[index] for index in starting_locations]

n = len(instructions)

lenghts = []

for j in range(len(pointer_nodes)):
    i = 0
    while not pointer_nodes[j].data.endswith('Z'):
        move_to = instructions[i % n]
        i += 1
        if move_to == 'R':
            pointer_nodes[j] = pointer_nodes[j].right
        elif move_to == 'L':
            pointer_nodes[j] = pointer_nodes[j].left
    lenghts.append(i)


print(lenghts)
print(lcm(*lenghts))

f.close()
