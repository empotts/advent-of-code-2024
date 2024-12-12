with open('input.txt', 'r') as file:
    input_data = [line.strip() for line in file]

print("Input Data:", input_data)

visited = set()

def find_coordinates(input_data, target):
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if char == target:
                return (x, y)
    return None

def turn_right(direction):
    directions = ['up', 'right', 'down', 'left']
    return directions[(directions.index(direction) + 1) % 4]

def move(x, y, direction):
    if direction == 'up':
        return x, y - 1
    elif direction == 'right':
        return x + 1, y
    elif direction == 'down':
        return x, y + 1
    elif direction == 'left':
        return x - 1, y

x,y = find_coordinates(input_data, '^')
direction = 'up'
print("Coordinates:", x, y)

while True:
    visited.add((x, y))
    next_x, next_y = move(x, y, direction)
    
    if (0 <= next_x < len(input_data[0]) and 0 <= next_y < len(input_data) and input_data[next_y][next_x] != '#'):
        x, y = next_x, next_y
    else:
        direction = turn_right(direction)
    
    #print("Current Location:", x, y, "Direction:", direction)
    if (next_x < 0 or next_x >= len(input_data[0]) or next_y < 0 or next_y >= len(input_data)):
        break

print("Visited Locations:", visited)
print("Number of Visited Locations:", len(visited)) # Part 1 Answer
