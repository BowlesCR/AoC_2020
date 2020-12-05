import fileinput


seatIDs: set[int] = set()
for line in [line.rstrip() for line in fileinput.input()]:
    line = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    row = int(line[:7], 2)
    col = int(line[7:10], 2)

    seatIDs.add(row * 8 + col)

print(f"Part 1: {max(seatIDs)}, Part 2: {set(range(min(seatIDs), max(seatIDs))).difference(seatIDs).pop()}")