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

for counter in range(0, 10000):

    print("counter " + str(counter))

    len_monkey_0_items += len(monkey_0_items)
    for monkey_item in monkey_0_items:
        if (monkey_item * 5) % 3 == 0:
            monkey_7_items.append((monkey_item * 5) % 9699690)
        else:
            monkey_4_items.append((monkey_item * 5) % 9699690)
        monkey_0_items = []

    len_monkey_1_items += len(monkey_1_items)
    for monkey_item in monkey_1_items:
        if (monkey_item + 6) % 17 == 0:
            monkey_3_items.append((monkey_item + 6) % 9699690)
        else:
            monkey_0_items.append((monkey_item + 6) % 9699690)
        monkey_1_items = []

    len_monkey_2_items += len(monkey_2_items)
    for monkey_item in monkey_2_items:
        if (monkey_item + 5) % 2 == 0:
            monkey_3_items.append((monkey_item + 5) % 9699690)
        else:
            monkey_1_items.append((monkey_item + 5) % 9699690)
        monkey_2_items = []

    len_monkey_3_items += len(monkey_3_items)
    for monkey_item in monkey_3_items:
        if (monkey_item + 2) % 19 == 0:
            monkey_7_items.append((monkey_item + 2) % 9699690)
        else:
            monkey_0_items.append((monkey_item + 2) % 9699690)
        monkey_3_items = []

    len_monkey_4_items += len(monkey_4_items)
    for monkey_item in monkey_4_items:
        if (monkey_item * 7) % 11 == 0:
            monkey_5_items.append((monkey_item * 7) % 9699690)
        else:
            monkey_6_items.append((monkey_item * 7) % 9699690)
        monkey_4_items = []

    len_monkey_5_items += len(monkey_5_items)
    for monkey_item in monkey_5_items:
        if (monkey_item + 7) % 5 == 0:
            monkey_2_items.append((monkey_item + 7) % 9699690)
        else:
            monkey_1_items.append((monkey_item + 7) % 9699690)
        monkey_5_items = []

    len_monkey_6_items += len(monkey_6_items)
    for monkey_item in monkey_6_items:
        if (monkey_item + 1) % 13 == 0:
            monkey_5_items.append((monkey_item + 1) % 9699690)
        else:
            monkey_2_items.append((monkey_item + 1) % 9699690)
        monkey_6_items = []

    len_monkey_7_items += len(monkey_7_items)
    for monkey_item in monkey_7_items:
        if (monkey_item * monkey_item) % 7 == 0:
            monkey_4_items.append((monkey_item * monkey_item) % 9699690)
        else:
            monkey_6_items.append((monkey_item * monkey_item) % 9699690)
        monkey_7_items = []

print("len monkey 0 " + str(len_monkey_0_items))
print("len monkey 1 " + str(len_monkey_1_items))
print("len monkey 2 " + str(len_monkey_2_items))
print("len monkey 3 " + str(len_monkey_3_items))
print("len monkey 4 " + str(len_monkey_4_items))
print("len monkey 5 " + str(len_monkey_5_items))
print("len monkey 6 " + str(len_monkey_6_items))
print("len monkey 7 " + str(len_monkey_7_items))
