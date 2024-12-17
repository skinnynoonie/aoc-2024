# Assumptions:
# No machine will yield an infinite amount of combinations

import numpy

def parse_button(button):
    button_coords_split = button.strip().split(": ")[1].split(", ")
    x = int(button_coords_split[0].split("+")[1])
    y = int(button_coords_split[1].split("+")[1])
    return (x, y)

def parse_prize(prize):
    prize_coords_split = prize.strip().split(": ")[1].split(", ")
    x = int(prize_coords_split[0].split("=")[1])
    y = int(prize_coords_split[1].split("=")[1])
    return (x + 10000000000000, y + 10000000000000)

claw_machines = []
with open("input.txt", "r") as f:
    while True:
        button_a = parse_button(f.readline())
        button_b = parse_button(f.readline())
        prize = parse_prize(f.readline())
        claw_machines.append((button_a, button_b, prize))
       
        if f.readline() == "":
            break

# Uses system of equations to solve.
def find_solution(claw_machine):
    button_a = claw_machine[0]
    button_b = claw_machine[1]
    goal = claw_machine[2]
    matrix_one = numpy.array([
        [button_a[0], button_b[0]],
        [button_a[1], button_b[1]]
    ])
    matrix_two = numpy.array([goal[0], goal[1]])
    return numpy.linalg.solve(matrix_one, matrix_two)

result = 0
for claw_machine in claw_machines:
    solution = find_solution(claw_machine)
    solution_valid = (
        abs(solution[0] - round(solution[0])) <= 0.001 and
        abs(solution[1] - round(solution[1])) <= 0.001
    )
    if solution_valid:
        result += 3 * round(solution[0]) + round(solution[1])

print(result)
