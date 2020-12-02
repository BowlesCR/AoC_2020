import fileinput
import re

lines = [re.fullmatch(r"^(\d+)-(\d+) (\w): (\w+)$", line.rstrip()) for line in fileinput.input()]
print(sum([1 for m in lines if int(m.group(1)) <= m.group(4).count(m.group(3)) <= int(m.group(2))]))
