import os
day = os.path.basename(__file__).split('.')[0]


def algo1(data):
    elfs = data.split("\n\n")
    calories = [sum([int(x) for x in elf.split("\n") if x]) for elf in elfs]
    calories.sort(reverse=True)
    return calories[0]


def algo2(data):
    elfs = data.split("\n\n")
    calories = [sum([int(x) for x in elf.split("\n") if x]) for elf in elfs]
    calories.sort(reverse=True)
    return sum(calories[0:3])


if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = f.read()


    test1_input = \
"""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
    test1_answer = 24000
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    print("Answer 1: ", algo1(input_data))

    test2_answer = 45000
    if algo2(test1_input) == test2_answer:
        print("Second Question Test Passed")
    else:
        print("Second Question Test FAILED")

    print("Answer 2: ", algo2(input_data))
