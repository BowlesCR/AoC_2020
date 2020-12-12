import fileinput
from copy import deepcopy


class Seats:
    seats: list[list[chr]]

    def __init__(self, data: list[list[chr]]):
        self.seats = data

    def __eq__(self, other):
        return self.seats == other.seats

    def next(self):
        newseats = deepcopy(self.seats)

        for r, row in enumerate(self.seats):
            for c, seat in enumerate(row):
                if seat == '.':
                    continue

                count = self.countAdjacent(r, c)
                if seat == "L":
                    if count == 0:
                        newseats[r][c] = "#"
                elif seat == "#":
                    if count >= 4:
                        newseats[r][c] = "L"

        return Seats(newseats)

    def countAdjacent(self, r: int, c: int):
        count: int = 0

        if r - 1 >= 0:
            seats = self.seats[r - 1][max(c - 1, 0):min(c + 2, len(self.seats[r - 1]))]
            count += sum([1 for seat in seats if seat == "#"])

        if r + 1 < len(self.seats):
            seats = self.seats[r + 1][max(c - 1, 0):min(c + 2, len(self.seats[r + 1]))]
            count += sum([1 for seat in seats if seat == "#"])

        if c - 1 >= 0 and self.seats[r][c - 1] == "#":
            count += 1

        if c + 1 < len(self.seats[r]) and self.seats[r][c + 1] == "#":
            count += 1

        return count

    def print(self):
        return
        for r in self.seats:
            print("".join(r))
        print()

    def numOccupied(self):
        count = 0
        for r in self.seats:
            count += sum([1 for seat in r if seat == '#'])
        return count


def main() -> None:
    seats = Seats([list(line.rstrip()) for line in fileinput.input()])
    seats.print()
    while True:
        newseats = seats.next()
        newseats.print()
        if seats == newseats:
            print(seats.numOccupied())
            break
        seats = newseats


if __name__ == "__main__":
    main()
