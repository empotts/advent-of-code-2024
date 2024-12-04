with open('input.txt', 'r') as file:
    input_data = [line.strip() for line in file]

print("Input Data:", input_data)
count = 0
for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        length = len(input_data[i])
        if input_data[i][j] == 'S':
            words = []
            if j <= length - 4:
                words.append(input_data[i][j:j+4])
            if j >= 4 - 1:
                words.append(input_data[i][j:j-4:-1])
            if i <= len(input_data) - 4:
                words.append(input_data[i][j] + input_data[i+1][j] + input_data[i+2][j] + input_data[i+3][j])
            if i >= 4 - 1:
                words.append(input_data[i][j] + input_data[i-1][j] + input_data[i-2][j] + input_data[i-3][j])
            if i <= len(input_data) - 4 and j <= length - 4:
                words.append(input_data[i][j] + input_data[i+1][j+1] + input_data[i+2][j+2] + input_data[i+3][j+3])
            if i >= 4 - 1 and j <= length - 4:
                words.append(input_data[i][j] + input_data[i-1][j+1] + input_data[i-2][j+2] + input_data[i-3][j+3])
            if i <= len(input_data) - 4 and j >= 4 - 1:
                words.append(input_data[i][j] + input_data[i+1][j-1] + input_data[i+2][j-2] + input_data[i+3][j-3])
            if i >= 4 - 1 and j >= 4 - 1:
                words.append(input_data[i][j] + input_data[i-1][j-1] + input_data[i-2][j-2] + input_data[i-3][j-3])
            print("Words:", words)
            #count += words.count("XMAS") # Idk why starting with X didn't work lmao 
            count += words.count("SAMX")
print("Count:", count) # Part 1 Answer



count2 = 0
for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        length = len(input_data[i])
        if input_data[i][j] == 'A':
            if i > 0 and i < len(input_data) - 1 and j > 0 and j < length - 1:
                emms = 0
                esses = 0
                if input_data[i-1][j-1] == 'M':
                    emms += 1
                if input_data[i-1][j-1] == 'S':
                    esses += 1
                if input_data[i+1][j-1] == 'M':
                    emms += 1
                if input_data[i+1][j-1] == 'S':
                    esses += 1
                if input_data[i-1][j+1] == 'M':
                    emms += 1
                if input_data[i-1][j+1] == 'S':
                    esses += 1
                if input_data[i+1][j+1] == 'M':
                    emms += 1
                if input_data[i+1][j+1] == 'S':
                    esses += 1
                if emms == esses ==2:
                    if input_data[i-1][j-1] != input_data[i+1][j+1]:
                        count2 += 1
print("Count 2:", count2) # Part 2 Answer
                