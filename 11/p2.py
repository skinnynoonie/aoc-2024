all_stones = []
[all_stones.append(number) for number in open("input.txt").readline().split(" ")]

def blink(stone):
    stones = {stone: 1}
    for i in range(75):
        stones_updates = {}
        for stone in stones.keys():
            if stone == "0":
                stones_updates["1"] = (stones_updates["1"] if "1" in stones_updates else 0) + stones[stone]
            elif len(stone) % 2 == 0:
                stone_one = stone[0:len(stone) // 2]
                stone_two = stone[len(stone) // 2:]
                stone_one = str(int(stone_one))
                stone_two = str(int(stone_two))
                stones_updates[stone_one] = (stones_updates[stone_one] if stone_one in stones_updates else 0) + stones[stone]
                stones_updates[stone_two] = (stones_updates[stone_two] if stone_two in stones_updates else 0) + stones[stone]
            else:
                new_stone = str(int(stone) * 2024)
                stones_updates[new_stone] = (stones_updates[new_stone] if new_stone in stones_updates else 0) + stones[stone]
        stones = stones_updates
    
    total = 0
    for stone_count in stones.values():
        total += stone_count
    return total

result = 0
for stone in all_stones:
    result += blink(stone)
print(result)
