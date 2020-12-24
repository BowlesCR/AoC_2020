import fileinput
from collections import defaultdict, deque
from math import sin, cos, pi

tPoint = tuple[float, float]


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


def neighbor(point: tPoint, d: str) -> tPoint:
    dist = 2

    if d == "e":
        return point[0] + dist, point[1]
    elif d == "se":
        a = 300 * pi / 180
    elif d == "sw":
        a = 240 * pi / 180
    elif d == "w":
        return point[0] - dist, point[1]
    elif d == "nw":
        a = 120 * pi / 180
    elif d == "ne":
        a = 60 * pi / 180
    else:
        raise Exception(d)

    x = round(point[0] + dist * cos(a), 2)
    y = round(point[1] + dist * sin(a), 2)

    return x, y


if __name__ == "__main__":
    main()
