import fileinput


def main() -> None:
    heading = 90
    x = 0
    y = 0

    for line in fileinput.input():
        action = line[0]
        value = int(line[1:])

        if action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "E":
            x += value
        elif action == "W":
            x -= value
        elif action == "L":
            heading -= value
            if heading < 0:
                heading += 360
        elif action == "R":
            heading += value
            if heading >= 360:
                heading -= 360
        elif action == "F":
            if heading == 0:
                y += value
            elif heading == 180:
                y -= value
            elif heading == 90:
                x += value
            elif heading == 270:
                x -= value
            else:
                raise Exception(heading)

    print(abs(x)+abs(y))


if __name__ == "__main__":
    main()
