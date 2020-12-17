import fileinput
import re
import itertools


def main() -> None:
    reRule = re.compile(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)")

    rules: dict[str, tuple[range, range]] = {}

    tickets: list[list[int]] = []

    for line in fileinput.input():
        line = line.rstrip()
        if line == "" or line == "your ticket:" or line == "nearby tickets:":
            continue

        m = reRule.fullmatch(line)
        if m:
            rules[m.group(1)] = (
                range(int(m.group(2)), int(m.group(3)) + 1),
                range(int(m.group(4)), int(m.group(5)) + 1),
            )
        else:
            tickets.append([int(f) for f in line.split(",")])

    errorrate = 0

    for ticket in tickets[1:]:
        for f in ticket:
            if all([f not in itertools.chain(r[0], r[1]) for r in rules.values()]):
                errorrate += f

    print(errorrate)


if __name__ == "__main__":
    main()
