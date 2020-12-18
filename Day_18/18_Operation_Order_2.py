import fileinput
from math import prod


def main() -> None:
    lines: list[str] = [line for line in fileinput.input()]

    sum = 0
    for line in [Line(line.rstrip()) for line in lines]:
        sum += line.solve_all()

    print(sum)


class Line:
    tokens: list[str]

    def __init__(self, line):
        self.tokens = line.replace("(", "( ").replace(")", " )").split(" ")

    def solve_parens(self, tokens: list[str]) -> (list[str], int):
        newTokens = []

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == "(":
                paren = self.solve_parens(tokens[i + 1:])

                newTokens.extend(paren[0])

                i += paren[1]
            elif token == ")":
                return [str(self.solve(newTokens))], i + 1
            else:
                newTokens.append(token)

            i += 1

        return [str(self.solve(newTokens))], -1

    def solve_all(self):
        tokens: list[str] = self.solve_parens(self.tokens)[0]
        return self.solve(tokens)

    @staticmethod
    def solve(tokens: list[str]) -> int:
        newTokens = []

        oper = None

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isnumeric():
                if not oper:
                    newTokens.append(token)
                else:
                    newTokens.append(str(int(newTokens.pop()) + int(token)))
                    oper = None
            elif token == "+":
                oper = token
            elif token == "*":
                pass
            else:
                newTokens.append(token)

            i += 1

        return prod([int(token) for token in newTokens])


if __name__ == "__main__":
    main()
