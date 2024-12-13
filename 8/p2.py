map = []

for line in open("input.txt").readlines():
    map.append(line.strip())

x_len = len(map)
y_len = len(map[0])

nodes = []
for x in range(x_len):
    for y in range(y_len):
        if map[x][y] != ".":
            nodes.append((x, y, map[x][y]))

results = set()
for node in nodes:
    for x in range(x_len):
        for y in range(y_len):
            if (x == node[0] and y == node[1]):
                continue
            if (map[x][y] != node[2]):
                continue
            slope = (x - node[0], y - node[1])
            
            x_look_ahead = node[0]
            y_look_ahead = node[1]
            while 0 <= x_look_ahead + slope[0] < x_len and 0 <= y_look_ahead + slope[1] < y_len:
                results.add((x_look_ahead + slope[0], y_look_ahead + slope[1]))
                x_look_ahead += slope[0]
                y_look_ahead += slope[1]

print(len(results))