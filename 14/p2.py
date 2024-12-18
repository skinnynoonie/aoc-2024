height = 103
width = 101

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

seconds = 0
while True:
    robot_positions = set()
    for robot in robots:
        position = robot[0]
        velocity = robot[1]
        robot[0] = (
            (position[0] + velocity[0]) % width, 
            (position[1] + velocity[1]) % height
        )
        robot_positions.add(robot[0])

    seconds += 1

    for robot_pos in robot_positions:
        found_horizontal = 1
        
        look_ahead_y = 1
        for i in range(10):
            if (robot_pos[0], robot_pos[1] + look_ahead_y) in robot_positions:
                found_horizontal += 1
                look_ahead_y += 1
            else:
                break
        
        if found_horizontal >= 8:
            for y in range(height):
                for x in range(width):
                    if (x, y) in robot_positions:
                        print("#", end="")
                    else:
                        print(".", end="")
                print()
            input(f"{seconds} seconds have passed. Press enter to continue.")
            break
