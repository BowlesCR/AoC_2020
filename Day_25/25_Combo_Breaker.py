import fileinput

def main() -> None:
    with fileinput.input() as fi:
        cardpub = int(fi.readline())
        doorpub = int(fi.readline())


    cardloop: int = 0
    doorloop: int = 0

    value = 1
    i = 1
    while True:
        value *= 7
        value %= 20201227

        if value == cardpub:
            cardloop = i
            break
        if value == doorpub:
            doorloop = i
            break

        i += 1

    if cardloop:
        value = 1
        for _ in range(cardloop):
            value *= doorpub
            value %= 20201227
        print(value)
    elif doorloop:
        value = 1
        for _ in range(doorloop):
            value *= cardpub
            value %= 20201227
        print(value)
    else:
        raise Exception("Neither loop value found!")


if __name__ == "__main__":
    main()
