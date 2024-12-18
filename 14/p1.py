height = 103
width = 101
seconds = 100

robots = []

for line in open("input.txt").readlines():
    position_unparsed = line.split(" ")[0].split("=")[1]
    velocity_unparsed = line.split(" ")[1].split("=")[1]
   
    position = (
        int(position_unparsed.split(",")[0]),
        int(position_unparsed.split(",")[1])
    )
   
    velocity = (
        int(velocity_unparsed.split(",")[0]),
        int(velocity_unparsed.split(",")[1])
    )
   
    robots.append([position, velocity])

for robot in robots:
    position = robot[0]
    velocity = robot[1]
    robot[0] = (
        (position[0] + velocity[0] * seconds) % width,
        (position[1] + velocity[1] * seconds) % height
    )

middle_vertical = width // 2
middle_horizontal = height // 2

quadrants = [0, 0, 0, 0]
for robot in robots:
    position = robot[0]
    if position[0] < middle_vertical and position[1] < middle_horizontal:
        quadrants[0] += 1
    if position[0] > middle_vertical and position[1] < middle_horizontal:
        quadrants[1] += 1
    if position[0] < middle_vertical and position[1] > middle_horizontal:
        quadrants[2] += 1
    if position[0] > middle_vertical and position[1] > middle_horizontal:
        quadrants[3] += 1

result = 1
for quadrant in quadrants:
    result *= quadrant
print(result)
