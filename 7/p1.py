number_to_numbers = []

for line in open("input.txt").readlines():
    line_split = line.split(": ")
    number_to_numbers.append((int(line_split[0]), [int(n) for n in line_split[1].split(" ")]))

def recursive_compute(numbers, current_value, current_index, goal_value):
    current_number = numbers[current_index]
    if current_index == len(numbers) - 1:
        return (
            current_value + current_number == goal_value or
            current_value * current_number == goal_value
        )
   
    return (
        recursive_compute(numbers, current_value + current_number, current_index + 1, goal_value) or
        recursive_compute(numbers, current_value * current_number, current_index + 1, goal_value)
    )

result = 0
for number_and_numbers in number_to_numbers:
    if (recursive_compute(number_and_numbers[1], 0, 0, number_and_numbers[0])):
        result += number_and_numbers[0]
print(result)
