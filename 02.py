import os
day = os.path.basename(__file__).split('.')[0]

score_map = {
    'X': 1, 'Y': 2, 'Z': 3,
    'A': 1, 'B': 2, 'C': 3
}

def rps(p1, p2):
    if p1 == p2:
        return 0
    if p1 == 'X' and p2 == 'B':
        return 2
    if p1 == 'Y' and p2 == 'C':
        return 2
    if p1 == 'Z' and p2 == 'A':
        return 2

    return 1

def lose(x):
    if x == 'A':
        return 'Z'
    if x == 'B':
        return 'X'
    if x == 'C':
        return 'Y'

def win(x):
    if x == 'A':
        return 'Y'
    if x == 'B':
        return 'Z'
    if x == 'C':
        return 'X'

def algo1(data):
    score = 0
    for round in data:
        them, me = round.split(" ")
        score += score_map[me]
        if score_map[them] == score_map[me]:
            score += 3
        elif rps(me, them) == 1:
            score += 6
    return score


def algo2(data):
    score = 0
    for round in data:
        them, outcome = round.split(" ")
        if outcome == 'Y':  # draw
            score += score_map[them] + 3
        elif outcome == 'X':  # lose
            score += score_map[lose(them)]
        else:  # win
            score += score_map[win(them)] + 6
    return score



if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test1_input = ["A Y",
        "B X",
        "C Z"]
    test1_answer = 15
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    print("Answer 1: ", algo1(input_data))

    test2_input = ["A Y",
        "B X",
        "C Z"]
    test2_answer = 12
    if algo2(test2_input) == test2_answer:
        print("Second Question Test Passed")
    else:
        print("Second Question Test FAILED")

    print("Answer 2: ", algo2(input_data))
