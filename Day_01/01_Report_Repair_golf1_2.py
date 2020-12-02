from itertools import combinations
import fileinput

print(
    [
        x * y * z
        for x, y, z in combinations([int(s) for s in fileinput.input()], 3)
        if x + y + z == 2020
    ][0]
)
