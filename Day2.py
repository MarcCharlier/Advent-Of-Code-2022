TotalScore = 0
with open('RockPaperScissors.txt') as f:
    while True:
        rps = str.strip(f.readline())
        if not rps:
            break
        if rps == 'A X':
            TotalScore += 3 #4
        elif rps == 'A Y':
            TotalScore += 4 #8
        elif rps == 'A Z':
            TotalScore += 8 #3
        elif rps == 'B X':
            TotalScore += 1 #1
        elif rps == 'B Y':
            TotalScore += 5 #5
        elif rps == 'B Z':
            TotalScore += 9 #9
        elif rps == 'C X':
            TotalScore += 2 #7
        elif rps == 'C Y':
            TotalScore += 6 #2
        elif rps == 'C Z':
            TotalScore += 7 #6
        print(rps + ' ' + str(TotalScore))
print(str(TotalScore))
