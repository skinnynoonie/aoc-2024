x_pos = 0
y_pos = 0
obstacle_map = []
for index, row in enumerate(open("input.txt").readlines()):
  obstacle_map.append(row.strip())
  if "^" in row:
    x_pos = index
    y_pos = row.index("^")

x_len = len(obstacle_map)
y_len = len(obstacle_map[0])

visited = set()
face = 0
face_directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

while True:
  face = face % 4
  direction = face_directions[face]

  visited.add((x_pos, y_pos))

  x_pos += direction[0]
  y_pos += direction[1]

  if x_pos < 0 or x_pos >= x_len or y_pos < 0 or y_pos >= y_len:
    break

  if obstacle_map[x_pos][y_pos] == "#":
    x_pos -= direction[0]
    y_pos -= direction[1]
    face += 1

print(len(visited))
