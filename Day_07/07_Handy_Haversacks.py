import fileinput
import re
from functools import lru_cache
from MCounter import MCounter


bags: dict[str, MCounter] = {}


def main() -> None:

    rColor = re.compile(r"^(\w+ \w+) bags contain")
    rContains = re.compile(r"(\d+) (\w+ \w+) bags?")
    for line in fileinput.input():
        color = rColor.match(line)[1]

        lst = MCounter()
        matches = rContains.findall(line)
        for m in matches:
            lst += MCounter({m[1]: int(m[0])})
        bags[color] = lst

    print(f"Part 1: {sum([1 for bag in bags if bag != 'shiny gold' and 'shiny gold' in unpack(bag)])}")
    print(f"Part 2: {sum(unpack('shiny gold').values()) - 1}")


@lru_cache
def unpack(bag) -> MCounter:
    result = MCounter({bag: 1})
    for b in bags[bag]:
        result += unpack(b) * bags[bag][b]
    return result


if __name__ == "__main__":
    main()
