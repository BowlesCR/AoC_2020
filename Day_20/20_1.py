import fileinput
from functools import lru_cache
from math import sqrt, prod
from typing import Optional
from itertools import combinations

tobin = str.maketrans("#.", "10")
t_gridChr = list[list[chr]]

minCount = 9999

class Tile:
    tileId: int
    grid: t_gridChr
    edges: list[set[int]]
    orientation: int

    neighbors: int

    def __init__(self, tileId: int = -1, grid: t_gridChr = None, tile = None):
        if tile:
            self.tileId = tile.tileId
            self.grid = tile.copyGrid()
            self.edges = tile.edges
            self.orientation = tile.orientation
            self.neighbors = tile.neighbors
        else:
            self.tileId = tileId
            self.grid = grid
            self.edges = []
            for i in range(4):
                self.edges.append(set())
                self.find_edges(i)
            self.orientation = 0
            self.neighbors = 0
            # print(self.edges)

    def copyGrid(self) -> t_gridChr:
        return [row.copy() for row in self.grid]

    def find_edges(self, orientation: int) -> None:
        # self.edges[orientation] = []

        newgrid: t_gridChr = self.copyGrid()

        if orientation == 1:
            newgrid.reverse()
        elif orientation == 2:
            for row in newgrid:
                row.reverse()
        elif orientation == 3:
            newgrid.reverse()
            for row in newgrid:
                row.reverse()

        self.edges[orientation].add(int("".join(newgrid[0]).translate(tobin), 2))  # Top
        self.edges[orientation].add(int("".join(newgrid[-1]).translate(tobin), 2))  # Bottom

        self.edges[orientation].add(int("".join([row[0] for row in newgrid]).translate(tobin), 2))  # Left
        self.edges[orientation].add(int("".join([row[-1] for row in newgrid]).translate(tobin), 2))  # Right

    def getEdges(self):
        return self.getEdges_o(self.orientation)

    @lru_cache
    def getEdges_o(self, o):
        return self.edges[o]

    def getAllEdges(self):
        return self.edges[0] | self.edges[1] | self.edges [2] | self.edges [3]

    def __str__(self) -> str:
        return str(self.tileId)

    def __repr__(self) -> str:
        return str(self.tileId)

    def copy(self):
        return Tile(tile=self)


t_gridTile = list[list[Optional[Tile]]]


def main() -> None:

    tiles: dict[int, Tile] = {}

    tileID: int
    grid: list[list[chr]] = []
    lines = [line.rstrip() for line in fileinput.input()]
    if lines[-1] != "":
        lines.append("")
    line: str
    for line in lines:
        if "Tile" in line:
            tileID = int(line.split(" ")[1][:-1])
        elif line == "":
            tiles[tileID] = Tile(tileID, grid)
            grid = []
        else:
            grid.append(list(line.rstrip()))
    del tileID, grid, lines, line

    for tile1, tile2 in combinations(tiles.values(), 2):
        if set(tile1.edges[0] | tile1.edges[1] | tile1.edges[2] | tile1.edges[3]).intersection(tile2.edges[0] | tile2.edges[1] | tile2.edges[2] | tile2.edges[3]):
            tile1.neighbors += 1
            tile2.neighbors += 1

    corners = [tile for tile in tiles if tiles[tile].neighbors == 2]

    print(prod(corners))

    dims = int(sqrt(len(tiles)))
    grid: t_gridTile = []
    for i in range(dims):
        grid.append([None]*dims)

    solution: Optional[t_gridTile] = None
    for corner in corners:


    for tile in tiles.values():

        for o in range(4):

            newTile = tile.copy()
            newTile.orientation = o

            newGrid = [row.copy() for row in grid]
            newGrid[0][0] = newTile

            newTiles = set(tiles.values())
            newTiles.remove(tile)

            print(f"{tile}.{o}")
            solution = arrangeTiles(newGrid, newTiles)
            print(f"  {minCount}")
            if solution:
                break
            # exit()

        if solution:
            print(prod([solution[0][0].tileId, solution[0][dims-1].tileId, solution[dims-1][0].tileId, solution[dims-1][dims-1].tileId]))
            exit()

def arrangeTiles(grid: t_gridTile, tiles: set[Tile]) -> Optional[t_gridTile]:
    global minCount

    if not tiles:
        return grid  # Success!

    minCount = min(minCount, len(tiles))

    for i in range(len(grid)):
        for r in range(i+1):
            for c in range(i+1):
                if grid[r][c]:
                    continue  # Already filled, move on
                if r > i or c > i:  # Force flood-fill from top left corner
                    continue

                hasUp = r > 0 and bool(grid[r - 1][c])
                # hasDown = r < len(grid) - 1 and bool(grid[r + 1][c])
                hasLeft = c > 0 and bool(grid[r][c - 1])
                # hasRight = c < len(grid[r]) - 1 and bool(grid[r][c + 1])

                for tile in tiles:
                    for o in range(4):
                        # if hasDown:  # Should never need this because of our iteration path, but meh
                            # if not checkMatch(grid[r+1][c], tile, o):
                            #     continue

                        if hasUp:
                            if not checkMatch(grid[r-1][c], tile, o):
                                continue

                        if hasLeft:
                            if not checkMatch(grid[r][c-1], tile, o):
                                continue

                        # if hasRight:  # Should never need this because of our iteration path, but meh
                            # if not checkMatch(grid[r][c+1], tile, o):
                            #     continue

                        newTiles = tiles.copy()
                        newTiles.remove(tile)

                        newTile = tile.copy()
                        newTile.orientation = o

                        newGrid = [row.copy() for row in grid]
                        newGrid[r][c] = newTile

                        solution = arrangeTiles(newGrid, newTiles)
                        if solution:
                            return solution
                return None

    raise Exception("This should be unreachable")


def checkMatch(tile1: Tile, tile2: Tile, orientation: int) -> bool:
    if tile1.getEdges() & tile2.edges[orientation]:
        return True
    return False


if __name__ == "__main__":
    main()
