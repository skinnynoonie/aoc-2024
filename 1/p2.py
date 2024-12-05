list_one = []
list_two = []

for line in open("input.txt").readlines():
  list_one.append(int(line.split("   ")[0]))
  list_two.append(int(line.split("   ")[1]))

result = 0
for i in range(0, len(list_one)):
  result += list_one[i] * list_two.count(list_one[i])

print(result)
