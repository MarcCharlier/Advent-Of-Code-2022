CaloriesCount = list()
CountCal = 0
with open('Calories.txt') as f:
    while True:
        CalLine = f.readline()
        if not CalLine:
            break
        if CalLine == '\n':
            CaloriesCount.append(CountCal)
            print('Calories ' + str(CaloriesCount[-1]))
            CountCal = 0
        else:
            CountCal += int(CalLine)
            print(CalLine.strip())
CaloriesCount.sort(reverse=True)
print(CaloriesCount[0])
TopThreeCal = CaloriesCount[0] + CaloriesCount[1] + CaloriesCount[2]
print(TopThreeCal)
