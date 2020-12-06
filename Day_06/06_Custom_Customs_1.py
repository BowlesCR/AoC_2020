import fileinput
from collections import Counter


def main() -> None:
    lines = [line.rstrip() for line in fileinput.input()]
    lines.append("")

    counter = Counter()
    total = 0
    for line in lines:
        if line == "":
            total += len(set(counter))
            counter = Counter()
        else:
            counter.update(line)

    print(total)


if __name__ == "__main__":
    main()
