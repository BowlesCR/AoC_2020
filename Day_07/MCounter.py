from collections import Counter


class MCounter(Counter):

    # whyTF isn't this built in?
    def __mul__(self, other):
        result = Counter()
        for _ in range(other):
            result += self
        return result
