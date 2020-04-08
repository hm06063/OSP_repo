#!/usr/bin/python3

if __name__ == '__main__':

    n = int(input("How many numbers do you wanna input?"))

    sum = 0

    for i in range(0,n):
        num = int(input("number to input: "))
        sum += num

    mean = sum/n

    print("the mean of numbers is {}".format(mean))
