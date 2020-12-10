import fileinput


def main() -> None:
    adapters = [int(line) for line in fileinput.input()]
    adapters.append(0)
    adapters.append(max(adapters)+3)
    adapters.sort()

    ones: int = 0
    threes: int = 0

    for i, a in enumerate(adapters):
        if i+1 < len(adapters):
            diff = adapters[i+1] - a
            if diff == 1:
                ones += 1
            elif diff == 3:
                threes += 1

    print(ones, threes, ones*threes)


if __name__ == "__main__":
    main()
