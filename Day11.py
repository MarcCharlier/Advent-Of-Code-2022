from math import trunc

monkey_0_items = [66, 71, 94]
monkey_1_items = [70]
monkey_2_items = [62, 68, 56, 65, 94, 78]
monkey_3_items = [89, 94, 94, 67]
monkey_4_items = [71, 61, 73, 65, 98, 98, 63]
monkey_5_items = [55, 62, 68, 61, 60]
monkey_6_items = [93, 91, 69, 64, 72, 89, 50, 71]
monkey_7_items = [76, 50]

len_monkey_0_items = 0
len_monkey_1_items = 0
len_monkey_2_items = 0
len_monkey_3_items = 0
len_monkey_4_items = 0
len_monkey_5_items = 0
len_monkey_6_items = 0
len_monkey_7_items = 0

for _ in range(0, 20):

    len_monkey_0_items += len(monkey_0_items)
    for monkey_item in monkey_0_items:
        if trunc(monkey_item * 5 / 3) % 3 == 0:
            monkey_7_items.append(trunc(monkey_item * 5 / 3))
        else:
            monkey_4_items.append(trunc(monkey_item * 5 / 3))
        monkey_0_items = []

    len_monkey_1_items += len(monkey_1_items)
    for monkey_item in monkey_1_items:
        if trunc((monkey_item + 6) / 3) % 17 == 0:
            monkey_3_items.append(trunc((monkey_item + 6) / 3))
        else:
            monkey_0_items.append(trunc((monkey_item + 6) / 3))
        monkey_1_items = []

    len_monkey_2_items += len(monkey_2_items)
    for monkey_item in monkey_2_items:
        if trunc((monkey_item + 5) / 3) % 2 == 0:
            monkey_3_items.append(trunc((monkey_item + 5) / 3))
        else:
            monkey_1_items.append(trunc((monkey_item + 5) / 3))
        monkey_2_items = []

    len_monkey_3_items += len(monkey_3_items)
    for monkey_item in monkey_3_items:
        if trunc((monkey_item + 2) / 3) % 19 == 0:
            monkey_7_items.append(trunc((monkey_item + 2) / 3))
        else:
            monkey_0_items.append(trunc((monkey_item + 2) / 3))
        monkey_3_items = []

    len_monkey_4_items += len(monkey_4_items)
    for monkey_item in monkey_4_items:
        if trunc(monkey_item * 7 / 3) % 11 == 0:
            monkey_5_items.append(trunc(monkey_item * 7 / 3))
        else:
            monkey_6_items.append(trunc(monkey_item * 7 / 3))
        monkey_4_items = []

    len_monkey_5_items += len(monkey_5_items)
    for monkey_item in monkey_5_items:
        if trunc((monkey_item + 7) / 3) % 5 == 0:
            monkey_2_items.append(trunc((monkey_item + 7) / 3))
        else:
            monkey_1_items.append(trunc((monkey_item + 7) / 3))
        monkey_5_items = []

    len_monkey_6_items += len(monkey_6_items)
    for monkey_item in monkey_6_items:
        if trunc((monkey_item + 1) / 3) % 13 == 0:
            monkey_5_items.append(trunc((monkey_item + 1) / 3))
        else:
            monkey_2_items.append(trunc((monkey_item + 1) / 3))
        monkey_6_items = []

    len_monkey_7_items += len(monkey_7_items)
    for monkey_item in monkey_7_items:
        if trunc(monkey_item * monkey_item / 3) % 7 == 0:
            monkey_4_items.append(trunc(monkey_item * monkey_item / 3))
        else:
            monkey_6_items.append(trunc(monkey_item * monkey_item / 3))
        monkey_7_items = []

print("len monkey 0 " + str(len_monkey_0_items))
print("len monkey 1 " + str(len_monkey_1_items))
print("len monkey 2 " + str(len_monkey_2_items))
print("len monkey 3 " + str(len_monkey_3_items))
print("len monkey 4 " + str(len_monkey_4_items))
print("len monkey 5 " + str(len_monkey_5_items))
print("len monkey 6 " + str(len_monkey_6_items))
print("len monkey 7 " + str(len_monkey_7_items))

