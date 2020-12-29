from __future__ import annotations
import fileinput
from functools import cached_property
from math import sqrt, prod
from typing import Optional, NamedTuple, Generator
from itertools import combinations, permutations
import re

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
        return {
            self.edges.top,
            self.edges.right,
            self.edges.bottom,
            self.edges.left,
        } | {
            self.rev_edges.top,
            self.rev_edges.right,
            self.rev_edges.bottom,
            self.rev_edges.left,
        }

    @cached_property
    def trim_edges(self):
        return [row[1:-1] for row in self.grid[1:-1]]

    def rotate(self) -> Tile:
        dim = len(self.grid[0])
        newGrid = []
        for i in range(dim):
            newGrid.append("".join(row[dim - 1 - i] for row in self.grid))
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

    print("Part 1:", prod(corners))

    dims = int(sqrt(len(tiles)))
    grid: t_gridTile = []
    for i in range(dims):
        grid.append([None] * dims)

    solution: Optional[t_gridTile] = None

    newTiles = set(tiles.values())
    for corner in corners:
        newTiles.remove(tiles[corner])

    for corners in permutations(corners, 4):
        for c1o in tiles[corners[0]].orientations():
            for c2o in tiles[corners[1]].orientations():
                for c3o in tiles[corners[2]].orientations():
                    for c4o in tiles[corners[3]].orientations():

                        newGrid = [row.copy() for row in grid]
                        newGrid[0][0] = c1o
                        newGrid[0][dims - 1] = c2o
                        newGrid[dims - 1][0] = c3o
                        newGrid[dims - 1][dims - 1] = c4o

                        # print(f"{c1o}")
                        solution = arrangeTiles(newGrid, newTiles)
                        # print(f"  {minCount}")
                        if solution:
                            break
                    if solution:
                        break
                if solution:
                    break
            if solution:
                break
        if solution:
            break
    del c1o, c2o, c3o, c4o
    del corner, corners
    del grid, newGrid, newTiles, tiles
    del i, tile1, tile2, dims

    grid: list[str] = []
    if solution:
        for row in solution:
            row = [tile.trim_edges for tile in row]
            for i in range(len(row[0])):
                grid.append("".join([tile[i] for tile in row]))

        del solution, row, i
        tile = Tile(tileId=0, grid=grid)
        del grid

        re1 = re.compile(r"(?=..................#.)")
        re2 = re.compile(r"#....##....##....###")
        re3 = re.compile(r".#..#..#..#..#..#...")

        for o in tile.orientations():
            monsters = 0
            for i, line in enumerate(o.grid[:-2]):
                for m1 in re1.finditer(line):
                    if re2.match(o.grid[i + 1], m1.start()) and re3.match(
                        o.grid[i + 2], m1.start()
                    ):
                        monsters += 1

            if monsters > 0:
                counthashes = sum([line.count("#") for line in o.grid])
                print("Part 2:", counthashes - (15 * monsters))
                exit()

    else:
        print("Fail.")


def arrangeTiles(grid: t_gridTile, tiles: set[Tile]) -> Optional[t_gridTile]:
    global minCount

    if not tiles:
        return grid  # Success!

    minCount = min(minCount, len(tiles))

    for i in range(len(grid)):
        for r in range(i + 1):
            for c in range(i + 1):
                if grid[r][c]:
                    continue  # Already filled, move on
                if r > i or c > i:  # Force flood-fill from top left corner
                    continue

                hasUp = r > 0 and bool(grid[r - 1][c])
                hasDown = r < len(grid) - 1 and bool(grid[r + 1][c])
                hasLeft = c > 0 and bool(grid[r][c - 1])
                hasRight = c < len(grid[r]) - 1 and bool(grid[r][c + 1])

                for tile in tiles:
                    for o in tile.orientations():
                        if hasDown:
                            if not checkAnyMatch(grid[r + 1][c], o, "down"):
                                break
                            if not checkMatch(grid[r + 1][c], o, "down"):
                                continue

                        if hasUp:
                            if not checkAnyMatch(grid[r - 1][c], o, "up"):
                                break
                            if not checkMatch(grid[r - 1][c], o, "up"):
                                continue

                        if hasLeft:
                            if not checkAnyMatch(grid[r][c - 1], o, "left"):
                                break
                            if not checkMatch(grid[r][c - 1], o, "left"):
                                continue

                        if hasRight:
                            if not checkAnyMatch(grid[r][c + 1], o, "right"):
                                break
                            if not checkMatch(grid[r][c + 1], o, "right"):
                                continue

                        newTiles = tiles.copy()
                        newTiles.remove(tile)

                        newGrid = [row.copy() for row in grid]
                        newGrid[r][c] = o

                        solution = arrangeTiles(newGrid, newTiles)
                        if solution:
                            return solution
                return None

    raise Exception("This should be unreachable")


def checkMatch(tile1: Tile, tile2: Tile, direction: str) -> bool:
    if direction == "left":
        return tile1.edges.right == tile2.edges.left
    elif direction == "right":
        return tile1.edges.left == tile2.edges.right
    elif direction == "up":
        return tile1.edges.bottom == tile2.edges.top
    elif direction == "down":
        return tile1.edges.top == tile2.edges.bottom

    raise Exception("This should be unreachable")


def checkAnyMatch(tile1: Tile, tile2: Tile, direction: str) -> bool:
    if direction == "left":
        return tile1.edges.right in tile2.all_edges
    elif direction == "right":
        return tile1.edges.left in tile2.all_edges
    elif direction == "up":
        return tile1.edges.bottom in tile2.all_edges
    elif direction == "down":
        return tile1.edges.top in tile2.all_edges

    raise Exception("This should be unreachable")


if __name__ == "__main__":
    main()
