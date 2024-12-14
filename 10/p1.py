map = []

for line in open("input.txt").readlines():
    map.append(line.strip())

x_len = len(map)
y_len = len(map[0])

def recursive_search(x, y, prev_number, discovered_nines):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        if not 0 <= x + direction[0] < x_len or not 0 <= y + direction[1] < y_len:
            continue

        number = int(map[x + direction[0]][y + direction[1]])
        if prev_number + 1 != number:
            continue

        if number == 9:
            discovered_nines.add((x + direction[0], y + direction[1]))
            continue

        recursive_search(x + direction[0], y + direction[1], number, discovered_nines)

    return len(discovered_nines)

result = 0
for x in range(x_len):
    for y in range(y_len):
        if map[x][y] == "0":
            result += recursive_search(x, y, 0, set())
print(result)
