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
                    if count >= 5:
                        newseats[r][c] = "L"

        return Seats(newseats)

    def countAdjacent(self, r: int, c: int):
        count: int = 0

        # East
        for tc in range(c+1, len(self.seats[r])):
            if self.seats[r][tc] == "L":
                break
            elif self.seats[r][tc] == "#":
                count += 1
                break

        # West
        for tc in range(c-1, -1, -1):
            if self.seats[r][tc] == "L":
                break
            elif self.seats[r][tc] == "#":
                count += 1
                break

        # North
        for tr in range(r-1, -1, -1):
            if self.seats[tr][c] == "L":
                break
            elif self.seats[tr][c] == "#":
                count += 1
                break

        # South
        for tr in range(r+1, len(self.seats)):
            if self.seats[tr][c] == "L":
                break
            elif self.seats[tr][c] == "#":
                count += 1
                break

        # NE
        for tr, tc in zip(range(r-1, -1, -1), range(c+1, len(self.seats[r]))):
            if self.seats[tr][tc] == "L":
                break
            elif self.seats[tr][tc] == "#":
                count += 1
                break

        # SE
        for tr, tc in zip(range(r+1, len(self.seats)), range(c+1, len(self.seats[r]))):
            if self.seats[tr][tc] == "L":
                break
            elif self.seats[tr][tc] == "#":
                count += 1
                break

        # NW
        for tr, tc in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
            if self.seats[tr][tc] == "L":
                break
            elif self.seats[tr][tc] == "#":
                count += 1
                break

        # SW
        for tr, tc in zip(range(r+1, len(self.seats)), range(c-1, -1, -1)):
            if self.seats[tr][tc] == "L":
                break
            elif self.seats[tr][tc] == "#":
                count += 1
                break

        return count

    def print(self):
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
    # seats.print()
    while True:
        newseats = seats.next()
        # newseats.print()
        if seats == newseats:
            print(seats.numOccupied())
            break
        seats = newseats


if __name__ == "__main__":
    main()
