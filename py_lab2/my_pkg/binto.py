#!/usr/bin/python3
def binto():
    userinput = input("input binary number : ")
    k = 1
    inputlen = len(userinput)
    num =0 

    for i in range(inputlen):

        if int(userinput[inputlen - i -1])==1:
            num += k
        k*=2
    print("=> OCT> {:#o}".format(num))
    print("=> DEC> {}".format(num))
    print("=> HEX> {:#x}".format(num))

    
    

