init_x_pos = 0
init_y_pos = 0
obstacle_map = []
for index, row in enumerate(open("input.txt").readlines()):
  obstacle_map.append(list(row.strip()))
  if "^" in row:
    init_x_pos = index
    init_y_pos = row.index("^")

x_len = len(obstacle_map)
y_len = len(obstacle_map[0])
face_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_original_path():
  face = 0
  x_pos = init_x_pos
  y_pos = init_y_pos
  visited = []

  while True:
    face = face % 4
    direction = face_directions[face]

    visited.append((x_pos, y_pos))

    x_pos += direction[0]
    y_pos += direction[1]

    if x_pos < 0 or x_pos >= x_len or y_pos < 0 or y_pos >= y_len:
      return visited

    if obstacle_map[x_pos][y_pos] == "#":
      x_pos -= direction[0]
      y_pos -= direction[1]
      face += 1

def path_is_looping():
  x_pos = init_x_pos
  y_pos = init_y_pos
  visited = set()
  face = 0

  while True:
    face = face % 4
    direction = face_directions[face]

    if (x_pos, y_pos, direction) in visited:
      return True
    
    visited.add((x_pos, y_pos, direction))

    x_pos += direction[0]
    y_pos += direction[1]

    if x_pos < 0 or x_pos >= x_len or y_pos < 0 or y_pos >= y_len:
      return False

    if obstacle_map[x_pos][y_pos] == "#" or obstacle_map[x_pos][y_pos] == "O":
      x_pos -= direction[0]
      y_pos -= direction[1]
      face += 1

results = set()
for coord in get_original_path()[1::]:
  obstacle_map[coord[0]][coord[1]] = "O"
  if path_is_looping():
    results.add(coord)
  obstacle_map[coord[0]][coord[1]] = "."

print(len(results))
