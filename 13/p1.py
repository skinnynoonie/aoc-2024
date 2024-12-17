def parse_button(button):
    button_coords_split = button.strip().split(": ")[1].split(", ")
    x = int(button_coords_split[0].split("+")[1])
    y = int(button_coords_split[1].split("+")[1])
    return (x, y)

def parse_prize(prize):
    prize_coords_split = prize.strip().split(": ")[1].split(", ")
    x = int(prize_coords_split[0].split("=")[1])
    y = int(prize_coords_split[1].split("=")[1])
    return (x, y)

claw_machines = []
with open("input.txt", "r") as f:
    while True:
        button_a = parse_button(f.readline())
        button_b = parse_button(f.readline())
        prize = parse_prize(f.readline())
        claw_machines.append((button_a, button_b, prize))
       
        if f.readline() == "":
            break

def find_all_combos(claw_machine):
    combos = []
   
    button_a = claw_machine[0]
    button_b = claw_machine[1]
    prize = claw_machine[2]
    for i in range(0, 101):
        for j in range(0, 101):
            x = button_a[0] * i + button_b[0] * j
            y = button_a[1] * i + button_b[1] * j
            if (x, y) == prize:
                combos.append((i, j))
   
    return combos

result = 0
for claw_machine in claw_machines:
    combos = find_all_combos(claw_machine)

    lowest_cost_combo = None
    for combo in combos:
        cost = combo[0] * 3 + combo[1]
        if lowest_cost_combo == None or cost < lowest_cost_combo:
            lowest_cost_combo = cost
   
    if lowest_cost_combo != None:
        result += lowest_cost_combo
   
print(result)
