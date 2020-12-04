import fileinput
import re


class Passport:
    data: dict[str, str]

    rYear = re.compile(r"\d{4}")
    rHeight = re.compile(r"(\d+)(cm|in)")
    rHexColor = re.compile(r"#[0-9a-f]{6}")
    rPID = re.compile(r"[0-9]{9}")

    def __init__(self) -> None:
        self.data = {}

    def isValid(self) -> bool:
        REQ_FIELDS: list[str] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        EYE_COLORS: list[str] = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if not all([field in self.data.keys() for field in REQ_FIELDS]):
            return False

        if not (
            self.rYear.fullmatch(self.data["byr"])
            and 1920 <= int(self.data["byr"]) <= 2002
        ):
            return False

        if not (
            self.rYear.fullmatch(self.data["iyr"])
            and 2010 <= int(self.data["iyr"]) <= 2020
        ):
            return False

        if not (
            self.rYear.fullmatch(self.data["eyr"])
            and 2020 <= int(self.data["eyr"]) <= 2030
        ):
            return False

        m = self.rHeight.fullmatch(self.data["hgt"])
        if not (
            m
            and (
                (m.group(2) == "cm" and 150 <= int(m.group(1)) <= 193)
                or (m.group(2) == "in" and 59 <= int(m.group(1)) <= 76)
            )
        ):
            return False

        if not self.rHexColor.fullmatch(self.data["hcl"]):
            return False

        if not self.data["ecl"] in EYE_COLORS:
            return False

        if not self.rPID.fullmatch(self.data["pid"]):
            return False

        return True

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
