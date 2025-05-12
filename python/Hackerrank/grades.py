
# N = 5
# inp = [['Harry', '37.21'], ['Berry', '37.21'], ['Tina', '37.2'], ['Akriti', '41'], ['Harsh', '39']]

# records = []

# for n in range(N):
#     name = inp[n][0]
#     score = float(inp[n][1])
#     student = [name, score]
#     records.append(student)
    
# records = sorted(records, key=lambda x: x[1])
    
# runner_up = []
# for i in range(1, (len(records) - 1)):
#     runner_up.append(records[i])
#     if records[i][1] != records[i+1][1]:
#         break

# runner_up.sort()

# for i in range(len(runner_up)):
#     print(runner_up[i][0])



N = 5
inp = [['Harry', '37.21'], ['Berry', '37.21'], ['Tina', '37.2'], ['Akriti', '41'], ['Harsh', '39']]

records = []

# Convert scores to floats and create the records list
for n in range(N):
    name = inp[n][0]
    score = float(inp[n][1])
    student = [name, score]
    records.append(student)

# Sort records by score (and by name if scores are equal)
records = sorted(records, key=lambda x: x[1])

# Find the second-lowest score
lowest_score = records[0][1]
second_lowest_score = None
for record in records:
    if record[1] > lowest_score:
        second_lowest_score = record[1]
        break

# Get all students with the second-lowest score
runner_up = [record[0] for record in records if record[1] == second_lowest_score]

# Sort names alphabetically
runner_up.sort()

# Print the names
for name in runner_up:
    print(name)