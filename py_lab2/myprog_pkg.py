#!/usr/bin/python3
from my_pkg import *


if __name__== '__main__':
    while(True):
        sel = int(input("Select menu: 1)Conversion 2) union/intersection 3) exit?"))
        if sel==1:
            binto.binto()
        elif sel ==2:
            uninter.uninter()
        else:
            print("exit the program...")
            break


