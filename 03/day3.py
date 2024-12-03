import re
with open('input.txt', 'r') as file:
    input_data = file.read()
#https://www.w3schools.com/python/python_regex.asp
#https://docs.python.org/3/library/re.html
pattern = re.compile(r'mul\((\d+),(\d+)\)')
sum = 0;
matches = pattern.findall(input_data)
for match in matches:
    num1, num2 = map(int, match)
    sum += num1 * num2

print("Sum:", sum) # Part 1 Answer


do_pattern = re.compile(r'do\(\)')
dont_pattern = re.compile(r"don't\(\)")

sum = 0
enabled = True  

index = 0
while index < len(input_data):
    if do_pattern.match(input_data, index):
        enabled = True
        index += len("do()")
    elif dont_pattern.match(input_data, index):
        enabled = False
        index += len("don't()")
    else:
        mul_match = pattern.match(input_data, index)
        if mul_match and enabled:
            num1, num2 = map(int, mul_match.groups())
            sum += num1 * num2
            index += len(mul_match.group(0))
        else:
            index += 1

print("Sum:", sum)  # Part 2 Answer