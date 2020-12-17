import fileinput
import re
from itertools import chain
from collections import defaultdict
from math import prod


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

    del line, reRule, m

    validtickets = tickets[:1]

    for ticket in tickets[1:]:
        if all([any([f in chain(r[0], r[1]) for r in rules.values()]) for f in ticket]):
            validtickets.append(ticket)

    del tickets

    fieldMap: dict[int, list[str]] = defaultdict(list)
    for i in range(len(validtickets[0])):
        for r in rules:
            if all(
                [
                    ticket[i] in chain(rules[r][0], rules[r][1])
                    for ticket in validtickets
                ]
            ):
                fieldMap[i].append(r)

    keepLooping = True
    while keepLooping:
        keepLooping = False
        for f in [v[0] for v in fieldMap.values() if len(v) == 1]:
            for v in fieldMap.values():
                if len(v) > 1 and f in v:
                    v.remove(f)
                    keepLooping = True

    print(
        prod(
            [
                validtickets[0][f]
                for f in fieldMap
                if fieldMap[f][0].startswith("departure")
            ]
        )
    )


if __name__ == "__main__":
    main()
