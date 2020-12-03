import fileinput


def main() -> None:
    m = [line.rstrip() for line in fileinput.input()]
    counter = 0
    h = len(m)
    w = len(m[0])
    x = 0
    y = 0
    while y < h:
        if x >= w:
            x -= w
        if m[y][x] == "#":
            counter += 1
        x += 3
        y += 1

    print(counter)


if __name__ == "__main__":
    main()
