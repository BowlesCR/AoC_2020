import fileinput
from collections import defaultdict, deque


tPoint = tuple[int, int]


def main() -> None:
    tiles: defaultdict[tPoint, bool] = defaultdict(bool)

    line: str
    for line in [line.rstrip() for line in fileinput.input()]:
        currentPoint: tPoint = (0, 0)

        chars = deque(line)
        while chars:
            d = chars.popleft()
            if d in ["n", "s"]:
                d += chars.popleft()

            currentPoint = neighbor(currentPoint, d)

        tiles[currentPoint] ^= True

    print(
        f"White: {len([t for t in tiles.values() if not t])}, Black: {len([t for t in tiles.values() if t])}"
    )

    for _ in range(100):
        ntiles = tiles.copy()

        for tile in list(tiles.keys()):

            for point in [tile] + all_neighbors(tile):

                blackneighbors = countblackneighbors(tiles, point)
                if tiles[point] and (blackneighbors == 0 or blackneighbors > 2):
                    ntiles[point] = False
                elif not tiles[point] and (blackneighbors == 2):
                    ntiles[point] = True

        tiles = ntiles
        if (_ + 1) % 10 == 0:
            print(f"Day {_+1}: {len([True for t in tiles.values() if t])}")


def neighbor(point: tPoint, d: str) -> tPoint:
    if d == "e":
        return point[0] + 2, point[1]
    elif d == "se":
        return point[0] + 1, point[1] - 1
    elif d == "sw":
        return point[0] - 1, point[1] - 1
    elif d == "w":
        return point[0] - 2, point[1]
    elif d == "nw":
        return point[0] - 1, point[1] + 1
    elif d == "ne":
        return point[0] + 1, point[1] + 1
    else:
        raise Exception(d)


def all_neighbors(point) -> list[tPoint]:
    return [
        neighbor(point, "e"),
        neighbor(point, "se"),
        neighbor(point, "sw"),
        neighbor(point, "w"),
        neighbor(point, "nw"),
        neighbor(point, "ne"),
    ]


def countblackneighbors(tiles: defaultdict[tPoint, bool], point: tPoint) -> int:
    count = 0
    for n in all_neighbors(point):
        if tiles[n]:
            count += 1
    return count


if __name__ == "__main__":
    main()
