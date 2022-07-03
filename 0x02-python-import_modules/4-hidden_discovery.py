#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    list1 = dir()
    for i in range(0, len(list1)):
        if list1[i][0:2] != "__":
            print("{}".format(list1[i]))
