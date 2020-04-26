#!/usr/bin/python3
def uninter():
    first = input("1st list: ")
    first = first[1:-1]
    first = first.replace(',',' ').split()
    first = list(map(int,first))
    
    sec = input("2nd list: ")
    sec = sec[1:-1]
    sec = sec.replace(',',' ').split()
    sec = list(map(int,sec))
    
    union = set(first).union(set(sec))
    print("=> union {}".format(list(union)))
    intersect = set(first).intersection(set(sec))
    print("=> intersection {}".format(list(intersect)))

