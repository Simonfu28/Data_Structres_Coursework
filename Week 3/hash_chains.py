# python3
# passes all test cases in 1.32 ms

import time

class node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

def store(head, string):
    x = node()
    if head.next != None:
        temp = head.next
        x.value = string
        x.next = temp
        temp.prev = x
        x.prev = head
        head.next = x
    else:
        head.next = x
        x.value = string
        x.prev = head

def delete(head, string):
    temp = head.next
    while temp is not None:
        if temp.value == string:
            x = temp.prev
            y = temp.next
            if y is not None:
                x.next = y
                y.prev = x
            else:
                x.next = None
        temp = temp.next
            
def find(head, string):
    temp = head.next
    while temp is not None:
        if temp.value == string:
            return True
        temp = temp.next
    return False

def check(head):
    temp = head.next
    outs = []
    while temp is not None:
        outs.append(temp.value)
        temp = temp.next
    return outs

def hash(m, string):
    h = 0
    for i, c in enumerate(string):
        x = ord(c)
        h = h + (x*(263**i))
        h = h%1000000007
    return h%m


if __name__ == "__main__":
    with open("hash_chains_tests/3.txt") as f:
        lines = f.read().splitlines()

    start = time.time()

    heads = []
    for i in range(0,int(lines[0])):
        heads.append(i)             ##Creates a list of heads of the linked lists
        heads[i] = node()
    
    for c in lines[1:]:
        i = c.split()
        h = heads[hash(int(lines[0]), i[1])]
        if i[0] == "add":
            if find(h, i[1]) is False:
                store(h, i[1])
        if i[0] == "del":
            if find(h, i[1]) is True:
                delete(h, i[1])
        if i[0] == "find":
            if find(h, i[1]) is True:
                print("yes")
            else:
                print("no")
        if i[0] == "check":
            x = int(i[1])
            out = check(heads[x])
            print(out)

    end = time.time()
    print("The time of execution of above program is :", (end-start) * 10**3, "ms")
    

        





        
