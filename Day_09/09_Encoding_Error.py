import fileinput
from itertools import combinations

PREAMBLE: int = 25


def main() -> None:
    data: list[int] = [int(line) for line in fileinput.input()]
    invalid: int = None
    for i, num in enumerate(data):
        if i < PREAMBLE:
            continue

        if num not in [sum(foo) for foo in combinations(data[i-PREAMBLE:i], 2)]:
            invalid = num
            print(f"Part 1: {invalid}")
            break

    if not invalid:
        raise Exception

    for i in range(len(data)):
        for j in range(i+2, len(data)):
            if sum(data[i:j]) == invalid:
                print(f"Part 2: {min(data[i:j]) + max(data[i:j])}")
                exit()


if __name__ == "__main__":
    main()
