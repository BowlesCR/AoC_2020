from itertools import combinations
import fileinput

print(
    [
        x * y
        for x, y in combinations([int(s) for s in fileinput.input()], 2)
        if x + y == 2020
    ][0]
)
