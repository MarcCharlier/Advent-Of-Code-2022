assignment_subsets = 0
assignment_overlaps = 0
with open('SectionPairs.txt') as f:
    while True:
        sectionPair = str.strip(f.readline())
        if not sectionPair: break
        print(sectionPair)
        sectionPair1 = sectionPair[0:sectionPair.find(',')]
        sectionPair2 = sectionPair[sectionPair.find(',') + 1:int(len(sectionPair))]
        sectionPair11 = int(sectionPair1[0:sectionPair1.find('-')])
        sectionPair12 = int(sectionPair1[sectionPair1.find('-') + 1:int(len(sectionPair1))])
        sectionPair21 = int(sectionPair2[0:sectionPair2.find('-')])
        sectionPair22 = int(sectionPair2[sectionPair2.find('-') + 1:int(len(sectionPair2))])
        if (sectionPair11 >= sectionPair21 and sectionPair12 <= sectionPair22) or \
                (sectionPair21 >= sectionPair11 and sectionPair22 <= sectionPair12):
            assignment_subsets += 1
            print('subsets ' + str(assignment_subsets))
        if (sectionPair21 <= sectionPair11 <= sectionPair22) or \
                (sectionPair21 <= sectionPair12 <= sectionPair22) or \
                (sectionPair11 <= sectionPair21 <= sectionPair12) or \
                (sectionPair11 <= sectionPair22 <= sectionPair12):
            assignment_overlaps += 1
            print('overlaps ' + str(assignment_overlaps))
