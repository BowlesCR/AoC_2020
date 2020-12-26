from __future__ import annotations
import fileinput
from functools import lru_cache, cached_property
from math import sqrt, prod
from typing import Optional, NamedTuple, Generator
from itertools import combinations

minCount = 9999

class Edges(NamedTuple):
    top: str
    right: str
    bottom: str
    left: str

class Tile:
    tileId: int
    grid: list[str]

    neighbors: int

    def __init__(self, tileId: int, grid: list[str]):
        self.tileId = tileId
        self.grid = grid

        self.neighbors = 0

    @cached_property
    def edges(self) -> Edges:
        return Edges(
            "".join(self.grid[0]),
            "".join(row[-1] for row in self.grid),
            "".join(self.grid[-1]),
            "".join(row[0] for row in self.grid),
        )

    @cached_property
    def rev_edges(self) -> Edges:
        return Edges(
            self.edges.top[::-1],
            self.edges.right[::-1],
            self.edges.bottom[::-1],
            self.edges.left[::-1],
        )

    @cached_property
    def all_edges(self) -> set[str]:
        return {self.edges.top, self.edges.right, self.edges.bottom, self.edges.left} | {self.rev_edges.top, self.rev_edges.right, self.rev_edges.bottom, self.rev_edges.left}

    @cached_property
    def inner_parts(self):
        return [row[1:-1] for row in self.grid[1:-1]]

    def rotate(self) -> Tile:
        dim = len(self.grid[0])
        newGrid = []
        for i in range(dim):
            newGrid.append("".join(row[i] for row in self.grid))
        return Tile(self.tileId, newGrid)

    def flip(self) -> Tile:
        return Tile(self.tileId, [line[::-1] for line in self.grid])

    def orientations(self) -> Generator[Tile, None, None]:
        tile = self
        yield tile

        for i in range(3):
            tile = tile.rotate()
            yield tile

        tile = tile.flip()
        yield tile

        for i in range(3):
            tile = tile.rotate()
            yield tile

    def is_corner(self) -> bool:
        return self.neighbors == 2

    def is_edge(self) -> bool:
        return self.neighbors == 3

    def is_middle(self) -> bool:
        return self.neighbors == 4

    def __str__(self) -> str:
        return str(self.tileId)

    def __repr__(self) -> str:
        return str(self.tileId)


t_gridTile = list[list[Optional[Tile]]]


def main() -> None:

    tiles: dict[int, Tile] = {}

    tileID: int
    grid: list[str] = []
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
            grid.append(line.rstrip())
    del tileID, grid, lines, line

    for tile1, tile2 in combinations(tiles.values(), 2):
        if tile1.all_edges.intersection(tile2.all_edges):
            tile1.neighbors += 1
            tile2.neighbors += 1

    corners = [tile for tile in tiles if tiles[tile].is_corner()]

    print(prod(corners))
    exit()

    dims = int(sqrt(len(tiles)))
    grid: t_gridTile = []
    for i in range(dims):
        grid.append([None]*dims)

    solution: Optional[t_gridTile] = None
    # for corner in corners:


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
