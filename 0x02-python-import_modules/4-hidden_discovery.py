#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_f = dir()
    for i in range(0, len(all_f)):
        if all_f[i][:2] != "__":
            print("{:s}".format(all_f[i]))
