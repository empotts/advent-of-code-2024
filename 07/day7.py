from itertools import product


with open('input.txt', 'r') as file:
    equations = []
    for line in file.readlines():
        test_value, numbers = line.split(': ')
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        equations.append((test_value, numbers))

print(equations) 

def evaluate_expression(numbers, operators):
    result = str(numbers[0])
    for i in range(len(operators)):
        if operators[i] == '+':
            result = str(int(result) + numbers[i + 1])
        elif operators[i] == '*':
            result = str(int(result) * numbers[i + 1])
        elif operators[i] == '-':  # part 2
            result += str(numbers[i + 1])
    return int(result)

def can_be_true(test_value, numbers):
    if len(numbers) == 1:
        return numbers[0] == test_value

    for operators in product('+*-', repeat=len(numbers) - 1):
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

total_calibration_result = 0

for test_value, numbers in equations:
    if can_be_true(test_value, numbers):
        total_calibration_result += test_value

print("Total Calibration Result:", total_calibration_result) 