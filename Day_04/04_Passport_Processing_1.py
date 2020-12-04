import fileinput


class Passport:
    data: dict[str, str]

    def __init__(self) -> None:
        self.data = {}

    def isValid(self) -> bool:
        REQ_FIELDS: list[str] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        return all([field in self.data.keys() for field in REQ_FIELDS])

    def addData(self, data: list[str]) -> None:
        self.data[data[0]] = data[1]


def main() -> None:
    lines = [line.rstrip() for line in fileinput.input()]
    lines.append("")

    validCount: int = 0

    passport = Passport()
    for line in lines:
        if line == "":
            if passport.isValid():
                validCount += 1
            passport = Passport()
        else:
            for token in line.split(" "):
                passport.addData(token.split(":"))

    print(validCount)


if __name__ == "__main__":
    main()
