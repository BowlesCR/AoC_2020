import fileinput
import re
from functools import lru_cache


class Rules:
    rules: dict[int, list[str]]

    def __init__(self):
        self.rules = {}

    def addRule(self, num: int, body: list[str]):
        self.rules[num] = body

    @lru_cache
    def resolveRule(self, rule: int) -> str:
        body = self.rules[rule]
        if len(body) == 1 and '"' in body[0]:
            return body[0].replace('"', "")

        result = ""

        for token in body:
            if token.isnumeric():
                result += self.resolveRule(int(token))
            elif token == "|":
                result += token
            else:
                raise Exception(token)

        return f"({result})"

    @lru_cache()
    def get_regex(self, rule: int) -> re.Pattern:
        return re.compile(f"({self.resolveRule(rule)})")


def main() -> None:
    reRule = re.compile(r"(\d+): (.*)")

    lines: list[str] = [line.rstrip() for line in fileinput.input()]

    rules = Rules()

    count = 0

    for line in lines:
        m = reRule.fullmatch(line)
        if m:
            rules.addRule(int(m.group(1)), m.group(2).split(" "))
        elif line == "":
            continue
        else:
            rule0 = rules.get_regex(0)
            if rule0.fullmatch(line):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
