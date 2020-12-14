import fileinput
import re
from copy import deepcopy


def main() -> None:
    maskline = re.compile(r"mask = (\w+)\n?")
    memline = re.compile(r"mem\[(\d+)] = (\d+)\n?")

    mask: str = ""
    mem: dict[int, int] = {}

    for line in fileinput.input():
        m = maskline.fullmatch(line)
        if m:
            mask = m.group(1)
        else:
            m = memline.fullmatch(line)
            addr: int = int(m.group(1))
            val: int = int(m.group(2))

            for addr in applymask(mask, addr):
                mem[addr] = val

    print(sum(mem.values()))


def applymask(mask: str, addr: int) -> list[int]:
    addr: list[chr] = list(f"{addr:b}")
    addr = (["0"] * (36 - len(addr))) + addr
    for i, j in [(i, j) for i, j in enumerate(mask) if j != "0"]:
        addr[i] = j

    return floataddr(addr)


def floataddr(addr: list[chr]) -> set[int]:
    result: set[int] = set()

    if "X" in addr:
        i = addr.index("X")

        for j in ["0", "1"]:
            rdda = deepcopy(addr)
            rdda[i] = j
            result.update(floataddr(rdda))
        return result
    else:
        a = int("".join(addr), 2)
        return {a}


if __name__ == "__main__":
    main()
