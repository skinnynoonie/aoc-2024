word_search = [line.strip() for line in open("input.txt").readlines()]
x_len = len(word_search)
y_len = len(word_search[0])

def find_xmas(x, y):
  if word_search[x][y] != "X":
    return 0
  
  movements = [
    (1, 0), (-1, 0),
    (0, 1), (0, -1),
    (1, 1), (1, -1),
    (-1, 1), (-1, -1)
  ]

  xmas_found = 0

  for movement in movements:
    failed = False
    x_look_ahead = x
    y_look_ahead = y
    for i in range(3):
      if not (x_look_ahead + movement[0] in range(x_len)) or not (y_look_ahead + movement[1] in range(y_len)):
        failed = True
        break
      x_look_ahead += movement[0]
      y_look_ahead += movement[1]

      if (
        (i == 0 and word_search[x_look_ahead][y_look_ahead] != "M") or
        (i == 1 and word_search[x_look_ahead][y_look_ahead] != "A") or
        (i == 2 and word_search[x_look_ahead][y_look_ahead] != "S")
      ):
        failed = True
        break
    if not failed:
      xmas_found += 1

  return xmas_found

result = 0
for x in range(x_len):
  for y in range(y_len):
    result += find_xmas(x, y)

print(result)
