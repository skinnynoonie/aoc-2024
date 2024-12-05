word_search = [line.strip() for line in open("input.txt").readlines()]
x_len = len(word_search)
y_len = len(word_search[0])

def find_xmas(x, y):
  if word_search[x][y] != "A":
    return 0
  
  movements = [
    (1, 1), (1, -1)
  ]

  mas_found = 0

  for movement in movements:
    lettersFound = []
    for i in range(2):
      direction = -1 if i == 0 else 1
      x_look_ahead = x + movement[0] * direction
      y_look_ahead = y + movement[1] * direction
      if not (x_look_ahead in range(x_len)) or not (y_look_ahead in range(y_len)):
        break
      lettersFound.append(word_search[x_look_ahead][y_look_ahead])

    if "M" in lettersFound and "S" in lettersFound:
      mas_found += 1

  return 1 if mas_found == 2 else 0

result = 0
for x in range(x_len):
  for y in range(y_len):
    result += find_xmas(x, y)

print(result)
