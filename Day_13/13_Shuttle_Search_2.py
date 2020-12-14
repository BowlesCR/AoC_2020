import fileinput


def main() -> None:
    lines: list[str] = [line.rstrip() for line in fileinput.input()]
    rawbusses = lines[1].split(",")
    busses = [int(bus) for bus in rawbusses if bus != "x"]

    first = 0
    for bus in rawbusses:
        if bus != "x":
            first = int(bus)
            break
    print(first)

    interval = max(busses)

    start = (((100171379229052 // interval) + 1) * interval) - rawbusses.index(str(interval))

    print(start)
    offsets = [(o, int(b)) for o, b in enumerate(rawbusses) if b != "x"]
    for i in range(start, start * 10, interval):
        fail = False
        for offset, bus in offsets:
            if (i + offset) % bus != 0:
                fail = True
                break
        if not fail:
            print(i)
            exit()
    print("No solution")


if __name__ == "__main__":
    main()
