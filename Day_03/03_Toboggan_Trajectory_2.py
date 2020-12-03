import fileinput
from math import prod


def main() -> None:
    m: list[str] = [line.rstrip() for line in fileinput.input()]
    h = len(m)
    w = len(m[0])

    trees: list[int] = []
    slope: tuple[int, int]
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        counter = 0
        x = 0
        y = 0

        while y < h:
            if x >= w:
                x -= w
            if m[y][x] == "#":
                counter += 1
            x += slope[0]
            y += slope[1]
        trees.append(counter)

    print(prod(trees))


if __name__ == "__main__":
    main()
