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

for id in range(storage_id)[::-1]:
    id_space_needed = disk.count(id)
    id_start_index = disk.index(id)

    space_indexes = []
    space_count = 0
    for i in range(len(disk)):
        if i > id_start_index:
            break
        if disk[i] == "*":
            space_count += 1
            if space_count == id_space_needed:
                space_indexes = list(range(i - (space_count - 1), i + 1))
                break
        else:
            space_count = 0

    if len(space_indexes) != 0:
        id_start_index = disk.index(id)
        for i in range(id_start_index, id_start_index + id_space_needed):
            if disk[i] == id:
                disk[i] = "*"

    for i in space_indexes:
        disk[i] = id

result = 0
for i in range(len(disk)):
    if disk[i] != "*":
        result += disk[i] * i
print(result)
