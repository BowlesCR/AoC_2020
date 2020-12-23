import fileinput


def main() -> None:
    cups: list[int] = [int(i) for i in list(fileinput.input())[0]]

    mincup = min(cups)
    maxcup = max(cups)

    cupcount = len(cups)

    i = 0
    for _ in range(100):
        currentlabel = cups[i]

        temp: list[int] = []
        for o in range(3):
            x = (i + 1 + o) % len(cups)
            temp.append(cups[x])
        for cup in temp:
            cups.remove(cup)

        destlabel = currentlabel - 1
        while True:
            if destlabel < mincup:
                destlabel += maxcup
            if destlabel in cups:
                destindex = cups.index(destlabel)
                for e, cup in enumerate(temp):
                    cups.insert(destindex + 1 + e, cup)
                break

            destlabel -= 1
        i = (cups.index(currentlabel) + 1) % cupcount

    print(cups)
    print("".join([str(c) for c in cups[cups.index(1) + 1 :] + cups[: cups.index(1)]]))


if __name__ == "__main__":
    main()
