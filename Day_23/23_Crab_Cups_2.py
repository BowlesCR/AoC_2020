from __future__ import annotations
import fileinput
from typing import Optional
from math import prod


class Node:
    def __init__(
        self,
        data: int,
        prevnode: Optional[Node] = None,
        nextnode: Optional[Node] = None,
    ):
        self.data = data
        self.prevnode: Optional[Node] = prevnode
        self.nextnode: Optional[Node] = nextnode

    def next(self) -> Node:
        return self.nextnode

    def prev(self) -> Node:
        return self.prevnode

    def set_next(self, target: Node):
        self.nextnode = target
        target.prevnode = self

    def __repr__(self):
        return str(self.data)


class CircularLinkedList:
    def __init__(self, data: list[int]):
        self.start_node: Optional[Node] = None
        self.jumplist: dict[int, Node] = {}

        prevnode: Optional[Node] = None
        for d in data:
            node = Node(d, prevnode)
            self.jumplist[d] = node
            if prevnode:
                prevnode.nextnode = node
            else:
                self.start_node = node
            prevnode = node
        self.start_node.prevnode = prevnode
        prevnode.nextnode = self.start_node

    def find(self, data) -> Node:
        return self.jumplist[data]

    def to_list(self) -> list[int]:
        result: list[int] = []

        nextnode = self.start_node
        while True:
            result.append(nextnode.data)
            nextnode = nextnode.next()
            if nextnode == self.start_node:
                break

        return result

    def __repr__(self):
        return str(self.to_list())

    def __str__(self):
        return self.to_list()


def main() -> None:
    cups: list[int] = [int(i) for i in list(fileinput.input())[0]]

    mincup = min(cups)
    maxcup = max(cups)

    cups.extend(range(maxcup + 1, 1_000_001))
    maxcup = 1_000_000

    cups: CircularLinkedList = CircularLinkedList(cups)

    currentCup = cups.start_node
    for _ in range(10_000_000):
        currentlabel = currentCup.data

        temp_start: Node = currentCup.next()
        temp_end: Node = temp_start.next().next()

        currentCup.set_next(temp_end.next())

        destlabel = currentlabel - 1
        while True:
            if destlabel < mincup:
                destlabel += maxcup
            if destlabel not in [
                temp_start.data,
                temp_start.next().data,
                temp_end.data,
            ]:
                dest = cups.find(destlabel)
                old_next = dest.next()
                temp_end.set_next(old_next)
                dest.set_next(temp_start)
                break

            destlabel -= 1

        currentCup = currentCup.next()

    one = cups.find(1)

    # result = ""
    # cup = one.next()
    # for _ in range(8):
    #     result += str(cup.data)
    #     cup = cup.next()
    # print(result)

    print(one.next().data * one.next().next().data)


if __name__ == "__main__":
    main()
