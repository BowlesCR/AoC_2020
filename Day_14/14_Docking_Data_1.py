import fileinput
import re

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
            mem[addr] = applymask(mask, val)

    print(sum(mem.values()))


def applymask(mask: str, val: int) -> int:
    val &= int(mask.replace("X", "1"), 2)
    val |= int(mask.replace("X", "0"), 2)
    return val


if __name__ == "__main__":
    main()
