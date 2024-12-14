map = []

for line in open("input.txt").readlines():
    map.append(line.strip())

x_len = len(map)
y_len = len(map[0])

def recursive_search(x, y, prev_number):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    successes = 0
    for direction in directions:
        if not 0 <= x + direction[0] < x_len or not 0 <= y + direction[1] < y_len:
            continue

        number = int(map[x + direction[0]][y + direction[1]])
        if prev_number + 1 != number:
            continue

        if number == 9:
            successes += 1
            continue

        successes += recursive_search(x + direction[0], y + direction[1], number)

    return successes

result = 0
for x in range(x_len):
    for y in range(y_len):
        if map[x][y] == "0":
            result += recursive_search(x, y, 0)
print(result)
