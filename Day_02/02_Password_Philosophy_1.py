import fileinput
import re


def main() -> None:
    r = re.compile(r"^(\d+)-(\d+) (\w): (\w+)$")
    count = 0
    for m in [r.fullmatch(line.rstrip()) for line in fileinput.input()]:
        if m and int(m.group(1)) <= m.group(4).count(m.group(3)) <= int(m.group(2)):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
