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
                        if self.parent[node] == -1:                     ## Checks if current node is the root
                                height[node] = 1
                        elif height[node] != 0:                         ## Checks if the current node has been visited before
                                continue
                        else:                           
                                while n != -1:                          ## Travels up the tree to the root, saving the path into a temp queue
                                        temp_queue.append(n)
                                        n = self.parent[n]
                                        if height[n] != 0:
                                                temp = height[n]
                                                break
                                for c, i in enumerate(temp_queue):      ## Saves the heighs of the nodes that the traversal has visited
                                        height[i] = len(temp_queue) - c + temp
                
                return max(height)


def main():
        tree = TreeHeight()
        for i in range(10, 24): ## Loads the Test Cases
                path = "/home/simon/Data_Structres_Coursework/Week 1/tree_height_tests/" + str(i)
                tree.read(path)
                t = '/home/simon/Data_Structres_Coursework/Week 1/tree_height_tests/' + str(i) + ".a"
                f = open(t, 'r').readline()             ## Prints the correct answer 
                print(tree.compute_height(), f)         ## Prints the answer outputted from the solution
threading.Thread(target=main).start()
