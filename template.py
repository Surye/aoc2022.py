import os
day = os.path.basename(__file__).split('.')[0]

def algo1(data):
    pass


def algo2(data):
    pass


if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test1_input = []
    test1_answer = 0
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    print("Answer 1: ", algo1(input_data))

    # test2_input = []
    # test2_answer = 0
    # if algo2(test2_input) == test2_answer:
    #     print("Second Question Test Passed")
    # else:
    #     print("Second Question Test FAILED")
    #
    # print("Answer 2: ", algo2(input_data))
