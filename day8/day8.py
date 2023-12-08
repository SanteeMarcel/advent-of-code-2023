import re

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
    right_destination = ''.join(re.findall(r'[A-Z]',  right_destination))
    left_destination =  ''.join(re.findall(r'[A-Z]',  left_destination))

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


pointer_node = value_to_node_map['AAA']
i = 0
n = len(instructions)

while pointer_node.data != 'ZZZ':
   move_to = instructions[i % n]
   i += 1
   if move_to == 'R':
      pointer_node = pointer_node.right
   if move_to == 'L':
      pointer_node = pointer_node.left

print(i)

f.close()
