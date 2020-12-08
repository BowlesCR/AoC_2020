import fileinput


def run(instructions: list[tuple[str, str]]) -> int:
    acc = 0
    pc = 0
    breadcrumbs: set[int] = set()
    limit = len(instructions)  # Avoids calling len() every loop of the while
    while pc < limit:
        if pc in breadcrumbs:
            return None

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
    return acc


def main() -> None:
    instructions: list[list[str]] = [line.rstrip().split(" ") for line in fileinput.input()]

    for i in range(len(instructions)):

        if instructions[i][0] == "acc":
            continue  # No point in trying, since it won't change.

        attempt = instructions[:]  # Shallow copy for efficiency
        attempt[i] = instructions[i][:]  # Deep copy just the line we're on

        if instructions[i][0] == "jmp":
            attempt[i][0] = "nop"
        elif instructions[i][0] == "nop":
            attempt[i][0] = "jmp"

        result = run(attempt)
        if result:
            print(result)
            break


if __name__ == "__main__":
    main()
