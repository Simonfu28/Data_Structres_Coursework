# python3
# solves 2/2 test cases in 0.1 ms

import time

phone_number_dict = {}
name_dict = {}

def addContact(phone_number, name):
    if name not in name_dict:
        name_dict[name] = phone_number
        phone_number_dict[phone_number] = name
    else:
        drop_key = name_dict[name]
        name_dict[name] = [phone_number]
        phone_number.pop(drop_key)
        phone_number[phone_number] = name


def delContact(phone_number):
    if phone_number in phone_number_dict:
        drop_key = phone_number_dict[phone_number]
        phone_number_dict.pop(phone_number)
        name_dict.pop(drop_key)

def findContact(phone_number):
    if phone_number in phone_number_dict:
        return phone_number_dict[phone_number]
    else:
        return "not found"


if __name__ == "__main__":
    with open("phone_book_input.txt") as f:
        lines = f.read().splitlines()
    start = time.time()
    
    for txt in lines:
        x = txt.split()
        if x[0] == "add":
            addContact(x[1], x[2])
        elif x[0] == "del":
            delContact(x[1])
        else:
            print(findContact(x[1]))

    end = time.time()
    print("The time of execution of above program is :", (end-start) * 10**3, "ms")