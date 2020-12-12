import fileinput


def main() -> None:
    pos: tuple[int, int] = (0, 0)
    wp: tuple[int, int] = (10, 1)

    for line in fileinput.input():
        action = line[0]
        value = int(line[1:])

        if action == "N":
            wp = (wp[0], wp[1] + value)
        elif action == "S":
            wp = (wp[0], wp[1] - value)
        elif action == "E":
            wp = (wp[0] + value, wp[1])
        elif action == "W":
            wp = (wp[0] - value, wp[1])
        elif action == "L" or action == "R":
            if action == "L":
                value = 360 - value

            if value == 90:
                wp = (wp[1], -wp[0])
            elif value == 180:
                wp = (-wp[0], -wp[1])
            elif value == 270:
                wp = (-wp[1], wp[0])
            else:
                raise Exception(value)

        elif action == "F":
            pos = (pos[0]+(value * wp[0]), pos[1]+(value*wp[1]))

    print(abs(pos[0])+abs(pos[1]))


if __name__ == "__main__":
    main()
