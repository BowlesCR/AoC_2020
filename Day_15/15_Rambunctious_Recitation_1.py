import fileinput


def main() -> None:
    input: list[int] = [int(num) for num in list(fileinput.input())[0].split(",")]

    nums = input[:-1]
    spoken: set[int] = set(nums)

    lastnum = input[-1]
    for i in range(len(nums), 2020 - 1):
        if lastnum not in spoken:
            spoken.add(lastnum)
            nums.append(lastnum)
            lastnum = 0
        else:
            nums.append(lastnum)
            lastnum = i - (len(nums) - 2 - nums[:-1][::-1].index(lastnum))

    print(lastnum)


if __name__ == "__main__":
    main()
