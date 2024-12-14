input = open("input.txt").readline().strip()

disk = []
storage_id = 0
for i in range(len(input)):
    number = int(input[i])
    if i % 2 == 0:
        [disk.append(storage_id) for _ in range(number)]
        storage_id += 1
    else:
        [disk.append("*") for _ in range(number)]

# brings the iteration amount down drastically (probably from billions to maybe thousands)
recent_space_index = 0
for block_index in range(len(disk))[::-1]:
    if disk[block_index] == "*":
        continue
    for space_index in range(recent_space_index, len(disk)):
        if space_index >= block_index:
            break
        if disk[space_index] == "*":
            disk[space_index] = disk[block_index]
            disk[block_index] = "*"
            recent_space_index = space_index
            break

result = 0
for i in range(len(disk)):
    if disk[i] != "*":
        result += disk[i] * i
print(result)
