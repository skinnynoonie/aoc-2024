map = []

for line in open("input.txt").readlines():
    map.append(line.strip())

x_len = len(map)
y_len = len(map[0])

ABOVE = 1
BELOW = 2
LEFT = 3
RIGHT = 4

global_visited = set()

def recursive_count_fence(x, y, type, needs_fencing_locations):
    area_counted = 1

    global_visited.add((x, y))

    directions = [(0, 1, ABOVE), (0, -1, BELOW), (-1, 0, LEFT), (1, 0, RIGHT)]
    for direction in directions:
        neighbour_x = x + direction[0]
        neighbour_y = y + direction[1]
        
        if not 0 <= neighbour_x < x_len or not 0 <= neighbour_y < y_len:
            needs_fencing_locations.append((x, y, direction[2]))
            continue

        neighbour_type = map[neighbour_x][neighbour_y]
        if (neighbour_type != type):
            needs_fencing_locations.append((x, y, direction[2]))
            continue

        if (neighbour_x, neighbour_y) in global_visited:
            continue
        
        area_counted += recursive_count_fence(neighbour_x, neighbour_y, type, needs_fencing_locations)[0]
    return (area_counted, needs_fencing_locations)

def count_sides(needs_fencing_locations):
    sides = 0

    while len(needs_fencing_locations) != 0:
        fencing_location = needs_fencing_locations.pop(0)
        direction_of_fence = fencing_location[2]

        if direction_of_fence == ABOVE or direction_of_fence == BELOW:
            x_look_ahead = 1
            while (fencing_location[0] + x_look_ahead, fencing_location[1], direction_of_fence) in needs_fencing_locations:
                needs_fencing_locations.remove((fencing_location[0] + x_look_ahead, fencing_location[1], direction_of_fence))
                x_look_ahead += 1
            
            x_look_ahead = -1
            while (fencing_location[0] + x_look_ahead, fencing_location[1], direction_of_fence) in needs_fencing_locations:
                needs_fencing_locations.remove((fencing_location[0] + x_look_ahead, fencing_location[1], direction_of_fence))
                x_look_ahead -= 1
        else:
            y_look_ahead = 1
            while (fencing_location[0], fencing_location[1] + y_look_ahead, direction_of_fence) in needs_fencing_locations:
                needs_fencing_locations.remove((fencing_location[0], fencing_location[1] + y_look_ahead, direction_of_fence))
                y_look_ahead += 1

            y_look_ahead = -1
            while (fencing_location[0], fencing_location[1] + y_look_ahead, direction_of_fence) in needs_fencing_locations:
                needs_fencing_locations.remove((fencing_location[0], fencing_location[1] + y_look_ahead, direction_of_fence))
                y_look_ahead -= 1

        sides += 1

    return sides

result = 0
for x in range(x_len):
    for y in range(y_len):
        if not (x, y) in global_visited:
            recursive_search = recursive_count_fence(x, y, map[x][y], [])
            result += recursive_search[0] * count_sides(recursive_search[1])
print(result)
