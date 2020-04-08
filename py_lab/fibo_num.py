#/usr/bin/python3
#import sys

def fibo(num):
    if num<2:
        return num
    a,b = 0,1
    for k in range(num-1):
        a,b = b, a+b
    return b 

if __name__=='__main__':
    n = int(input("fibonacci number?"))
    for i in range(1,n):
        print(fibo(i),end = ",")
    print(fibo(n))
    print("F{} = {}".format(n,fibo(n)))

