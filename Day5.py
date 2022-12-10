StacksOfCrates = \
    [['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'],
     ['S', 'R', 'M', 'D', 'W', 'P', 'F'],
     ['V', 'C', 'R', 'S', 'Z'],
     ['R', 'T', 'J', 'Z', 'P', 'H', 'G'],
     ['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'],
     ['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'],
     ['G', 'C', 'V', 'B', 'P', 'Q'],
     ['Z', 'B', 'P', 'N'],
     ['W', 'P', 'J']]

with open('ArrangementProcedure.txt') as ap:
    while True:
        ArrangementStep = str.strip(ap.readline()).split(' ')
        if ArrangementStep == ['']: break
        StackFrom = int(ArrangementStep[3])-1
        StackTo = int(ArrangementStep[5])-1
        craneStack = list()
        for _ in range(int(ArrangementStep[1])):
            lastItemFrom = StacksOfCrates[StackFrom][-1]
            craneStack.append(lastItemFrom)
            StacksOfCrates[StackFrom].pop()
        # added the loop below for exercise part 2
        for _ in range(int(ArrangementStep[1])):
            lastItemTo = craneStack[-1]
            craneStack.pop()
            StacksOfCrates[StackTo].append(lastItemTo)

print('final')
for i in range(8): print(str(StacksOfCrates[i][-1]))
