number_to_numbers = {}

for line in open("input.txt").readlines():
    line_split = line.split(": ")
    number_to_numbers[int(line_split[0])] = [int(n) for n in line_split[1].split(" ")]

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
for number in number_to_numbers.keys():
    if (recursive_compute(number_to_numbers[number], 0, 0, number)):
        result += number
       
print(result)
