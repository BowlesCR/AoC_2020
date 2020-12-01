from itertools import combinations
import fileinput


def main() -> None:
    s: str
    data: list[int] = [int(s) for s in fileinput.input()]
    x: int
    y: int
    for x, y in combinations(data, 2):
        if x + y == 2020:
            print(x * y)
            break


if __name__ == "__main__":
    main()
