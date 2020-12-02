import fileinput
import re


def main() -> None:
    r = re.compile(r"^(\d+)-(\d+) (\w): (\w+)$")
    count = 0
    for m in [r.fullmatch(line.rstrip()) for line in fileinput.input()]:
        if m:
            pos1 = int(m.group(1)) - 1
            pos2 = int(m.group(2)) - 1
            c = m.group(3)
            pwd = m.group(4)

            if pwd[pos1] != pwd[pos2] and (pwd[pos1] == c or pwd[pos2] == c):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
