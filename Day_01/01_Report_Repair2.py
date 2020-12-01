from itertools import combinations
import fileinput


def main() -> None:
    s: str
    data: list[int] = [int(s) for s in fileinput.input()]
    x: int
    y: int
    for x, y, z in combinations(data, 3):
        if x + y + z == 2020:
            print(x * y * z)
            break


if __name__ == "__main__":
    main()
