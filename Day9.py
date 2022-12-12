head_squares_list = []
current_head_square = [0, 0]
head_squares_list.append(current_head_square)
with open('motions.txt') as m:
    while True:
        motion = str.strip(m.readline())
        if not motion: break
        number_of_steps = int(motion[2:])
        if motion[0] == "U":
            for _ in range(0, number_of_steps):
                new_square = [current_head_square[0], current_head_square[1] + 1]
                head_squares_list.append(new_square)
                current_head_square = new_square
        if motion[0] == "D":
            for _ in range(0, number_of_steps):
                new_square = [current_head_square[0], current_head_square[1] - 1]
                head_squares_list.append(new_square)
                current_head_square = new_square
        if motion[0] == "L":
            for _ in range(0, number_of_steps):
                new_square = [current_head_square[0] - 1, current_head_square[1]]
                head_squares_list.append(new_square)
                current_head_square = new_square
        if motion[0] == "R":
            for _ in range(0, number_of_steps):
                new_square = [current_head_square[0] + 1, current_head_square[1]]
                head_squares_list.append(new_square)
                current_head_square = new_square

tail_squares_list = []
current_tail_square = [0, 0]
new_tail_square = [0, 0]
tail_squares_list.append(new_tail_square)
for square_coordinate in head_squares_list:
    print("head_square " + str(square_coordinate))
    print("tail_square " + str(current_tail_square))
    if abs(square_coordinate[0] - current_tail_square[0]) > 1 or abs(square_coordinate[1] - current_tail_square[1]) > 1:
        if square_coordinate[0] == current_tail_square[0]:
            new_tail_square = [current_tail_square[0], int((square_coordinate[1] + current_tail_square[1]) / 2)]
        elif square_coordinate[1] == current_tail_square[1]:
            new_tail_square = [int((square_coordinate[0] + current_tail_square[0]) / 2), current_tail_square[1]]
        elif square_coordinate[0] > current_tail_square[0] and square_coordinate[1] > current_tail_square[1]:
            new_tail_square = [current_tail_square[0] + 1, current_tail_square[1] + 1]
        elif square_coordinate[0] > current_tail_square[0] and square_coordinate[1] < current_tail_square[1]:
            new_tail_square = [current_tail_square[0] + 1, current_tail_square[1] - 1]
        elif square_coordinate[0] < current_tail_square[0] and square_coordinate[1] > current_tail_square[1]:
            new_tail_square = [current_tail_square[0] - 1, current_tail_square[1] + 1]
        elif square_coordinate[0] < current_tail_square[0] and square_coordinate[1] < current_tail_square[1]:
            new_tail_square = [current_tail_square[0] - 1, current_tail_square[1] - 1]
        print("new tail square "+str(new_tail_square))
    tail_squares_list.append(new_tail_square)
    current_tail_square = new_tail_square

tail_squares_list_unique = []
count_squares = 0
for tail_square in tail_squares_list:
    if tail_square not in tail_squares_list_unique:
        count_squares += 1
        tail_squares_list_unique.append(tail_square)

print(str(count_squares))
