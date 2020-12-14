import fileinput


def main() -> None:
    lines: list[str] = [line.rstrip() for line in fileinput.input()]
    earliest = int(lines[0])
    busses = [int(bus) for bus in lines[1].split(",") if bus != "x"]

    minWait = (float("inf"), 0)
    for bus in busses:
        next = (((earliest // bus) + 1) * bus)
        wait = next - earliest
        if wait < minWait[0]:
            minWait = (wait, bus)

    print(minWait[0] * minWait[1])


if __name__ == "__main__":
    main()
