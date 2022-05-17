# python3
# passes 5/5 test cases, O(1) time

import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max = ""

    def Push(self, a):
        if self.max:
            if self.max < a:
                self.max = a
        else:
            self.max = a
        self.__stack.append(self.max)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop(-1)
        self.__stack.pop(-1)
        self.max = self.__stack[-2]

    def Max(self):
        return self.__stack[-2]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert 0
