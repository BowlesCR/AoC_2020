import fileinput
import re

lines = [re.fullmatch(r"^(\d+)-(\d+) (\w): (\w+)$", line.rstrip()) for line in fileinput.input()]
print(sum([1 for m in lines if (m.group(4)[int(m.group(1)) - 1] == m.group(3)) ^ (m.group(4)[int(m.group(2)) - 1] == m.group(3))]))
