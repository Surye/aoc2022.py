import os
day = os.path.basename(__file__).split('.')[0]

import string

item_priority = string.ascii_lowercase + string.ascii_uppercase

def item_value(item):
    return item_priority.index(item) + 1

def algo1(data):
    total = 0
    for pack in data:
        part1 = pack[0:len(pack)//2]
        part2 = pack[len(pack)//2:]
        same = list(set(part1).intersection(part2))[0]
        total += item_value(same)
    return total

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def algo2(data):
    total = 0
    for team in chunks(data, 3):
        same = list(set(team[0]).intersection(team[1]).intersection(team[2]))[0]
        total += item_value(same)
    return total


if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test1_input = ["vJrwpWtwJgWrhcsFMMfFFhFp",
                   "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                   "PmmdzqPrVvPwwTWBwg",
                   "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                   "ttgJtRGJQctTZtZT",
                   "CrZsJsPPZsGzwwsLwLmpwMDw"]

    test1_answer = 157
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    print("Answer 1: ", algo1(input_data))

    test2_input = test1_input
    test2_answer = 70
    if algo2(test2_input) == test2_answer:
        print("Second Question Test Passed")
    else:
        print("Second Question Test FAILED")

    print("Answer 2: ", algo2(input_data))
