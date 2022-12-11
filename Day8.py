from treegrid import tree_map

tree_map = tree_map()
tree_map_size = len(tree_map[0])-1

visible_count = (tree_map_size+1) * 2 + (tree_map_size - 1) * 2
highest_scenic_score = 0
for x in range(1, tree_map_size):
    for y in range(1, tree_map_size):
        scenic_score = 0
        is_tree_visible_d1 = True
        scenic_score_d1 = 0
        for d1 in reversed(range(0, y)):
            scenic_score_d1 += 1
            if tree_map[x][d1] >= tree_map[x][y]:
                is_tree_visible_d1 = False
                break
        is_tree_visible_d2 = True
        scenic_score_d2 = 0
        for d2 in range(y + 1, tree_map_size + 1):
            scenic_score_d2 += 1
            if tree_map[x][d2] >= tree_map[x][y]:
                is_tree_visible_d2 = False
                break
        is_tree_visible_d3 = True
        scenic_score_d3 = 0
        for d3 in reversed(range(0, x)):
            scenic_score_d3 += 1
            if tree_map[d3][y] >= tree_map[x][y]:
                is_tree_visible_d3 = False
                break
        is_tree_visible_d4 = True
        scenic_score_d4 = 0
        for d4 in range(x + 1, tree_map_size + 1):
            scenic_score_d4 += 1
            if tree_map[d4][y] >= tree_map[x][y]:
                is_tree_visible_d4 = False
                break
        if is_tree_visible_d1 or is_tree_visible_d2 or is_tree_visible_d3 or is_tree_visible_d4: visible_count += 1
        if scenic_score_d1 * scenic_score_d2 * scenic_score_d3 * scenic_score_d4 >= highest_scenic_score:
            highest_scenic_score = scenic_score_d1 * scenic_score_d2 * scenic_score_d3 * scenic_score_d4

print("visible count " + str(visible_count))
print("highest scenic score " + str(highest_scenic_score))
