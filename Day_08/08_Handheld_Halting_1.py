import fileinput


def run(instructions: list[tuple[str, str]]) -> int:
    acc = 0
    pc = 0
    breadcrumbs: set[int] = set()
    limit = len(instructions)  # Avoids calling len() every loop of the while
    while pc < limit:
        if pc in breadcrumbs:
            return acc

        breadcrumbs.add(pc)

        tokens = instructions[pc]
        if tokens[0] == "acc":
            acc += int(tokens[1])
        elif tokens[0] == "nop":
            pass
        elif tokens[0] == "jmp":
            pc += int(tokens[1])
            continue

        pc += 1


def main() -> None:
    instructions: list[tuple[str, str]] = [tuple(line.rstrip().split(" ")) for line in fileinput.input()]
    print(run(instructions))


if __name__ == "__main__":
    main()
