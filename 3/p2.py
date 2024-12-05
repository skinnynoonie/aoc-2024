import re

result = 0
enabled = True
for match in re.finditer(r"(do\(\))|(don't\(\))|(mul\(\d+,\d+\))", "".join(open("input.txt").readlines())):
  cmd = match.group(0)
  if cmd == "do()":
    enabled = True
  elif cmd == "don't()":
    enabled = False
  elif enabled:
    mul_cmd_args = cmd.replace("mul(", "").replace(")", "").split(",")
    result += int(mul_cmd_args[0]) * int(mul_cmd_args[1])

print(result)
