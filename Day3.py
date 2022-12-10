common_items = list()
# Part 1
with open('Rucksacks.txt') as f:
    while True:
        rucksack = str.strip(f.readline())
        if not rucksack: break
        rucksack1 = sorted(list(set(rucksack[0:int(len(rucksack) / 2)])))
        rucksack2 = sorted(list(set(rucksack[int(len(rucksack) // 2):int(len(rucksack))])))
        for rucksack_item in rucksack1:
            if rucksack_item in rucksack2:
                common_items.append(rucksack_item)
total_priorities = 0
for common_item in common_items:
    if str(common_item).islower():
        total_priorities += ord(common_item)-96
    else:
        total_priorities += ord(common_item)-38
print('Total priorities: ' + str(total_priorities))
# Part 2
badges = list()
with open('Rucksacks.txt') as f:
    while True:
        rucksackA = str.strip(f.readline())
        if not rucksackA: break
        rucksackB = str.strip(f.readline())
        if not rucksackB: break
        rucksackC = str.strip(f.readline())
        if not rucksackC: break
        rucksack_contentA = sorted(list(set(rucksackA)))
        rucksack_contentB = sorted(list(set(rucksackB)))
        rucksack_contentC = sorted(list(set(rucksackC)))
        for rucksack_item in rucksack_contentA:
            if rucksack_item in rucksack_contentB and rucksack_item in rucksack_contentC:
                badges.append(rucksack_item)
total_badges = 0
for badge in badges:
    if str(badge).islower():
        total_badges += ord(badge) - 96
    else:
        total_badges += ord(badge) - 38
print('Total badges: ' + str(total_badges))
