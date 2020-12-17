import fileinput
from collections import defaultdict
from copy import deepcopy

t_coords = tuple[int, int, int]


def inactive() -> chr:
    return "."


class Grid:
    grid: defaultdict[t_coords, chr]
    maxX: int = 0
    minX: int = 0
    maxY: int = 0
    minY: int = 0
    maxZ: int = 0
    minZ: int = 0

    def __init__(self):
        self.grid = defaultdict(inactive)

    def updateBounds(self, coords: t_coords) -> None:
        self.maxX = max(self.maxX, coords[0])
        self.minX = min(self.minX, coords[0])
        self.maxY = max(self.maxY, coords[1])
        self.minY = min(self.minY, coords[1])
        self.maxZ = max(self.maxZ, coords[2])
        self.minZ = min(self.minZ, coords[2])

    def add(self, coords: t_coords, state: chr):
        self.grid[coords] = state
        self.updateBounds(coords)

    def count_neighbors(self, coords: t_coords) -> int:
        result = 0
        for x in range(coords[0] - 1, coords[0] + 2):
            for y in range(coords[1] - 1, coords[1] + 2):
                for z in range(coords[2] - 1, coords[2] + 2):
                    if (x, y, z) != coords and self.grid[(x, y, z)] == "#":
                        result += 1
        return result

    def cycle(self):
        newGrid = deepcopy(self.grid)

        for x in range(self.minX - 1, self.maxX + 2):
            for y in range(self.minY - 1, self.maxY + 2):
                for z in range(self.minZ - 1, self.maxZ + 2):

                    cube: t_coords = (x, y, z)
                    neighbors = self.count_neighbors(cube)

                    if self.grid[cube] == "#" and neighbors not in [2, 3]:
                        newGrid[cube] = "."
                        self.updateBounds(cube)
                    elif self.grid[cube] == "." and neighbors == 3:
                        newGrid[cube] = "#"
                        self.updateBounds(cube)

        self.grid = newGrid

    def countActive(self):
        return sum([1 for state in self.grid.values() if state == "#"])


def main() -> None:
    lines: list[str] = [line.rstrip() for line in fileinput.input()]
    grid = Grid()
    for y, line in enumerate(lines):
        for x, state in enumerate(line):
            grid.add((x, y, 0), state)

    for _ in range(6):
        grid.cycle()

    print(grid.countActive())


if __name__ == "__main__":
    main()
