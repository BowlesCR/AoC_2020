import fileinput
from collections import Counter


def main() -> None:
    lines = [line.rstrip() for line in fileinput.input()]
    lines.append("")

    counter = Counter()
    total = 0
    groupsize = 0
    for line in lines:
        if line == "":
            total += len([i for i in counter.items() if i[1] == groupsize])
            counter = Counter()
            groupsize = 0
        else:
            groupsize += 1
            counter.update(line)

    print(total)


if __name__ == "__main__":
    main()
