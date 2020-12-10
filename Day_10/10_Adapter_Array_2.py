import fileinput
from functools import lru_cache


class Bag:
    adapters: set[int]
    target: int

    def __init__(self, adapters: list[int]):
        self.adapters = set(adapters)
        self.target = max(adapters) + 3
        self.adapters.add(self.target)

    @lru_cache()
    def count(self, current: int) -> int:
        result = 0

        if current == self.target:
            return 1

        if current + 1 in self.adapters:
            result += self.count(current + 1)

        if current + 2 in self.adapters:
            result += self.count(current + 2)

        if current + 3 in self.adapters:
            result += self.count(current + 3)

        return result


def main() -> None:

    b = Bag([int(line) for line in fileinput.input()])
    print(b.count(0))


if __name__ == "__main__":
    main()
