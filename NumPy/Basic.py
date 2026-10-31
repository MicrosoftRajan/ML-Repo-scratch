marks = [90, 92,95,97,98,91,99]

total = 0
for mark in marks:
    # print(mark)
# calculate Total = total + mark
    total = total + mark
    print(total)

count = 0
for mark in marks:

    count = count + 1
# Average Marks
    avg = total / count
    print("Average = ", avg)

highest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark
    print("Highest Marks: ", highest)


