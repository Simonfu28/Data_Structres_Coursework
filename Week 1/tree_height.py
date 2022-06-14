# python3
# passes 24/24 tests; 0.335 sec runtime on test #24

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self, path):
                #self.n = int(sys.stdin.readline())
                #self.parent = list(map(int, sys.stdin.readline().split()))
                f = open(path, 'r').readlines()
                self.n = int(f[0])
                self.parent = list(map(int, f[1].split()))


        def compute_height(self):
                height = [0]*self.n

                for node in range(0, self.n):
                        n = node
                        temp_queue = []
                        temp = 0
                        if self.parent[node] == -1:
                                height[node] = 1
                        elif height[node] != 0:
                                continue
                        else:
                                while n != -1:
                                        temp_queue.append(n)
                                        n = self.parent[n]
                                        if height[n] != 0:
                                                temp = height[n]
                                                break
                                for c, i in enumerate(temp_queue):
                                        height[i] = len(temp_queue) - c + temp
                
                return max(height)


def main():
        tree = TreeHeight()
        for i in range(10, 24):
                path = "/home/simon/Data_Structres_Coursework/Week 1/tree_height_tests/" + str(i)
                tree.read(path)
                t = '/home/simon/Data_Structres_Coursework/Week 1/tree_height_tests/' + str(i) + ".a"
                f = open(t, 'r').readline()
                print(tree.compute_height(), f)
threading.Thread(target=main).start()
