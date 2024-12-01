left_list = []
right_list = []

with open('input.txt', 'r') as file:
    input_data = file.readlines()

for line in input_data:
    left, right = line.split('   ') 
    left_list.append(int(left))
    right_list.append(int(right))

print("Left List:", left_list)
print("Right List:", right_list)

sorted_left = sorted(left_list)
sorted_right = sorted(right_list)

distances = []

for left, right in zip(sorted_left, sorted_right):
    distances.append(abs(left - right))

total_distance = sum(distances)

print("Total Distance:", total_distance) # Part 1 Answer


hash_map = {}
for left in left_list:
    occurrences = right_list.count(left)
    hash_map[left] = occurrences * left

hash_map_sum = sum(hash_map.values())
print("Sum of Hash Map Values:", hash_map_sum)