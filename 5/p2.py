# it works but takes a long time (my solution sucks)

pages = []
rules = []

pages_section = False
for line in open("input.txt").readlines():
  if line == "\n":
    pages_section = True
    continue

  if pages_section:
    pages.append([int(num) for num in line.split(",")])
  else:
    rules.append([int(num) for num in line.split("|")])

def isValid(page):
  for page_num_index in range(len(page)):
    page_num = page[page_num_index]
    for page_num_ahead_index in range(page_num_index + 1, len(page)):
      page_num_ahead = page[page_num_ahead_index]
      for rule in rules:
        if rule[0] == page_num_ahead and rule[1] == page_num:
          return False
  return True

def one_iter_fix_attempt(page):
  for page_num_index in range(len(page)):
    page_num = page[page_num_index]
    for page_num_ahead_index in range(page_num_index + 1, len(page)):
      page_num_ahead = page[page_num_ahead_index]
      for rule in rules:
        if rule[0] == page_num_ahead and rule[1] == page_num:
          page[page_num_index] = page_num_ahead
          page[page_num_ahead_index] = page_num
          return

result = 0      
for page in pages:
  if not isValid(page):
    while not isValid(page):
      one_iter_fix_attempt(page)
    result += page[len(page) // 2]

print(result)