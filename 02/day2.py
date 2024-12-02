with open('input.txt', 'r') as file:
    input_data = [list(map(int, line.split())) for line in file.readlines()]




print("Input Data:", input_data)
count = 0;
for lst in input_data:
    valid = True
    increasing = lst[0] < lst[1]
    for i in range(len(lst)-1):
        if increasing and lst[i] > lst[i+1]:
            valid = False
            break
        elif not increasing and lst[i] < lst[i+1]:
            valid = False
            break
        if abs(lst[i] -lst[i+1]) > 3 or abs(lst[i] -lst[i+1]) == 0:
            valid = False
            break
    if valid:
        count += 1
        print("Valid Password:", lst)


print("Valid Passwords:", count) # Part 1 Answer

def checkList(lst):
    increasing = lst[0] < lst[1]
    for i in range(len(lst)-1):
        if increasing and lst[i] > lst[i+1]:
            return False
        elif not increasing and lst[i] < lst[i+1]:
            return False
        if abs(lst[i] -lst[i+1]) > 3 or abs(lst[i] -lst[i+1]) == 0:
            return False
    return True


count = 0
for lst in input_data:
    if checkList(lst):
        count += 1
        print("Valid Password:", lst)
    else:
        valid = False
        for i in range(len(lst)):
            tempList = lst[:i] + lst[i+1:]
            if checkList(tempList):
                count += 1
                valid = True
                break
        if valid:
            print("Valid Password after removal:", lst)

print("Total Valid Passwords:", count)