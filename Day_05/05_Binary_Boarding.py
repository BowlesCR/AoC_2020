import fileinput


seatIDs: set[int] = set()
for line in [line.rstrip() for line in fileinput.input()]:
    row = col = 0
    for c in line:
        if c == "F":
            row <<= 1
        elif c == "B":
            row = row << 1 | 1
        elif c == "L":
            col <<= 1
        elif c == "R":
            col = col << 1 | 1

    seatIDs.add(row * 8 + col)

print(max(seatIDs))
print(set(range(min(seatIDs), max(seatIDs))).difference(seatIDs).pop())
