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

    p1, p2 = play_game(p1, p2)

    winner: deque[int]
    if p1:
        winner = p1
    else:
        winner = p2

    score: int = 0
    for i, c in enumerate(reversed(winner), 1):
        score += i * c

    print(score)


def play_game(p1: deque[int], p2: deque[int]) -> (deque[int], deque[int]):
    states: set[str] = set()

    while p1 and p2:
        state = f"{','.join(str(x) for x in p1)} | {','.join(str(x) for x in p2)}"
        if state in states:
            return deque([1]), deque()
        states.add(state)

        p1c = p1.popleft()
        p2c = p2.popleft()

        if len(p1) >= p1c and len(p2) >= p2c:
            a, b = play_game(deque(list(p1)[:p1c]), deque(list(p2)[:p2c]))
            if a:
                p1.append(p1c)
                p1.append(p2c)
            else:
                p2.append(p2c)
                p2.append(p1c)

        elif p1c > p2c:
            p1.append(p1c)
            p1.append(p2c)
        else:
            p2.append(p2c)
            p2.append(p1c)

    return p1, p2


if __name__ == "__main__":
    main()
