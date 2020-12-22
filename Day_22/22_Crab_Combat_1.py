import fileinput
from collections import deque


def main() -> None:
    p1: deque[int] = deque()
    p2: deque[int] = deque()

    player = 1
    for line in fileinput.input():
        if "Player" in line:
            continue
        elif line == "\n":
            player = 2
            continue
        else:
            if player == 1:
                p1.append(int(line))
            else:
                p2.append(int(line))

    # print(p1)
    # print(p2)

    while p1 and p2:
        p1c = p1.popleft()
        p2c = p2.popleft()

        if p1c > p2c:
            p1.append(p1c)
            p1.append(p2c)
        else:
            p2.append(p2c)
            p2.append(p1c)

    # print(p1)
    # print(p2)

    winner: deque[int]
    if p1:
        winner = p1
    else:
        winner = p2

    score: int = 0
    for i, c in enumerate(reversed(winner), 1):
        score += i * c

    print(score)


if __name__ == "__main__":
    main()
