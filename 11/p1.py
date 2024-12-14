stones = []
[stones.append(number) for number in open("input.txt").readline().split(" ")]

for i in range(25):
    for stone_index in range(len(stones)):
        stone = stones[stone_index]
        if stone == "0":
            stones[stone_index] = "1"
        elif len(stone) % 2 == 0:
            stone_one = stone[0:len(stone) // 2]
            stone_two = stone[len(stone) // 2:]
            stone_one = str(int(stone_one))
            stone_two = str(int(stone_two))
            stones[stone_index] = stone_one
            stones.append(stone_two)
        else:
            stones[stone_index] = str(int(stone) * 2024)

print(len(stones))
