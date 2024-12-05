# Assumptions: 
# All reports will have more than 2 levels

reports = []
for line in open("input.txt").readlines():
  reports.append([int(level) for level in line.split(" ")])

def is_safe(report):
  if is_safe_strict(report):
    return True
  
  for i in range(0, len(report)):
    copy = report.copy()
    del copy[i]
    if is_safe_strict(copy):
      return True
    
  return False

def is_safe_strict(report):
  abs_difference = abs(report[1] - report[0])
  if abs_difference < 1 or abs_difference > 3:
    return False

  increasing = report[1] - report[0] > 0

  for i in range(2, len(report)):
    difference = report[i] - report[i - 1]
    if abs(difference) < 1 or abs(difference) > 3:
      return False
    if increasing and difference < 0:
      return False
    if not increasing and difference > 0:
      return False

  return True

safe = 0
for report in reports:
  if is_safe(report):
    safe += 1

print(safe)
