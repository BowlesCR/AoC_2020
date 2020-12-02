from itertools import combinations as cmb
import fileinput as fi
from math import prod

print([prod(c) for c in cmb([int(s) for s in fi.input()], 2) if sum(c) == 2020][0])
