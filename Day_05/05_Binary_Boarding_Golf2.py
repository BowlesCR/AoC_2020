import fileinput


seatIDs: set[int] = set([int(line.translate(str.maketrans("FBLR", "0101")), 2) for line in fileinput.input()])
print(f"Part 1: {max(seatIDs)}, Part 2: {set(range(min(seatIDs), max(seatIDs))).difference(seatIDs).pop()}")
