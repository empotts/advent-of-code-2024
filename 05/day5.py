def parse_input(input_data):
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.split('\n')]
    updates = [list(map(int, line.split(','))) for line in updates_section.split('\n')]
    return rules, updates

def is_correctly_ordered(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map and index_map[x] > index_map[y]:
            return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def order_update(update, rules):
    from collections import defaultdict, deque

    # Create a graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in update if in_degree[node] == 0])
    ordered_update = []

    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_update

with open('input.txt', 'r') as file:
    input_data = file.read()

def main(input_data):
    rules, updates = parse_input(input_data)
    middle_pages_sum_correct = 0
    middle_pages_sum_incorrect = 0
    for update in updates:
        if is_correctly_ordered(update, rules):
            middle_pages_sum_correct += find_middle_page(update)
        else:
            ordered_update = order_update(update, rules)
            middle_pages_sum_incorrect += find_middle_page(ordered_update)

    return middle_pages_sum_correct, middle_pages_sum_incorrect

correct_sum, incorrect_sum = main(input_data)
print("Sum of middle pages of correctly-ordered updates:", correct_sum)
print("Sum of middle pages of corrected updates:", incorrect_sum)