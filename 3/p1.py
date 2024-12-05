import re

result = 0
for match in re.finditer(r"mul\(\d+,\d+\)", "".join(open("input.txt").readlines())):
    mul_cmd = match.group(0)
    mul_cmd_args = mul_cmd.replace("mul(", "").replace(")", "").split(",")
    result += int(mul_cmd_args[0]) * int(mul_cmd_args[1])

print(result)
