map = []

for line in open("input.txt").readlines():
    map.append(line.strip())

x_len = len(map)
y_len = len(map[0])

global_visited = set()

def recursive_count_fence(x, y, type):
    fencing_needed = 0
    area_counted = 1

    global_visited.add((x, y))

    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for direction in directions:
        neighbour_x = x + direction[0]
        neighbour_y = y + direction[1]

        if not 0 <= neighbour_x < x_len or not 0 <= neighbour_y < y_len:
            fencing_needed += 1
            continue

        neighbour_type = map[neighbour_x][neighbour_y]
        if (neighbour_type != type):
            fencing_needed += 1
            continue

        if (neighbour_x, neighbour_y) in global_visited:
            continue
        
        neighbour_fencing_result = recursive_count_fence(neighbour_x, neighbour_y, type)
        fencing_needed += neighbour_fencing_result[0]
        area_counted += neighbour_fencing_result[1]
    return (fencing_needed, area_counted)

result = 0
for x in range(x_len):
    for y in range(y_len):
        if not (x, y) in global_visited:
            recursive_search = recursive_count_fence(x, y, map[x][y])
            result += recursive_search[0] * recursive_search[1] 
print(result)
