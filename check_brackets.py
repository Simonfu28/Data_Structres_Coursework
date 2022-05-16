# python3
import os
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
directory = "check_brackets tests"


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = [0]
    matching_brackets = {"(": ")", "{": "}", "[": "]"}
    last_open = 0
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(matching_brackets[next])
            last_open = i
            pass

        if next in ")]}":
            if next == opening_brackets_stack[-1]:
                opening_brackets_stack.pop(-1)
            else:
                return i+1
            pass

    if len(opening_brackets_stack) > 1:
        return last_open+1
    else:
        return "Success"

def solver(f):
    file = open(f, "r")
    return file.read()


def main():

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            if f[-1] != "a":
                file = open(f, "r")
                test_input = file.read()
                test_answer = solver((f + ".a"))
                mismatch = find_mismatch(test_input)
                if str(mismatch) == str(test_answer):
                    print(1)
                else:
                    print(mismatch, test_answer, f)


if __name__ == "__main__":
    main()
