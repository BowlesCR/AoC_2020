import fileinput
from itertools import combinations

PREAMBLE: int = 25


def main() -> None:
    data: list[int] = [int(line) for line in fileinput.input()]
    for i, num in enumerate(data):
        if i < PREAMBLE:
            continue
        if num not in [sum(foo) for foo in combinations(data[i-PREAMBLE:i], 2)]:
            print(num)
            break


if __name__ == "__main__":
    main()
