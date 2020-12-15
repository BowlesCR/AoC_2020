import fileinput


def main() -> None:
    input: list[int] = [int(num) for num in list(fileinput.input())[0].split(",")]

    spoken: dict[int, int] = {}

    for turn, num in enumerate(input[:-1]):
        spoken[num] = turn

    lastnum = input[-1]
    for i in range(len(spoken), 30000000 - 1):
        if lastnum not in spoken:
            spoken[lastnum] = i
            lastnum = 0
        else:
            temp = lastnum
            lastnum = i - spoken[lastnum]
            spoken[temp] = i

    print(lastnum)


if __name__ == "__main__":
    main()
