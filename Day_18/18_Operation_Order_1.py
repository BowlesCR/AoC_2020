import fileinput


def main() -> None:
    lines: list[str] = [line for line in fileinput.input()]

    sum = 0
    for line in [Line(line.rstrip()) for line in lines]:
        sum += line.solve()[0]

    print(sum)


class Line:
    tokens: list[str]

    def __init__(self, line):
        self.tokens = line.replace("(", "( ").replace(")", " )").split(" ")

    def solve(self, start: int = 0) -> (int, int):
        left = None
        oper = None
        i = start
        while i < len(self.tokens):
            token = self.tokens[i]
            if token.isnumeric():
                if not oper:
                    left = int(token)
                else:
                    left = self.domath(left, oper, int(token))
                    oper = None
            elif token in ["+", "*"]:
                oper = token
            elif token == "(":
                paren = self.solve(i + 1)
                if not oper:
                    left = paren[0]
                else:
                    left = self.domath(left, oper, paren[0])
                    oper = None
                i = paren[1]
            elif token == ")":
                return left, i
            else:
                raise Exception(token)

            i += 1

        return left, -1

    def domath(self, a: int, oper: str, b: int) -> int:
        if oper == "+":
            a += b
        elif oper == "*":
            a *= b

        return a


if __name__ == "__main__":
    main()
