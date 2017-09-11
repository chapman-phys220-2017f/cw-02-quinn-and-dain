#!/usr/bin/env python

def coord_for(n, a=0, b=1):
    coords = []
    dist = float((b-a)/n)
    #print(dist)
    for i in range(n+1):
        coords.append(a+i*dist)
    return coords

def coord_while(n, a=0, b=1):
    i = 0
    coords = []
    dist = float((b-a)/n)
    #print(dist)
    while((a+i)<=b):
        coords.append(a+i)
        i = i+dist
    return coords

def coord_comp(n, a=0, b=1):
    dist = float((b-a)/n)
    #print(dist)
    coords = [a+i*dist for i in range(n+1)]
    return coords

if __name__ == "__main__":
    #n,a,b = input("Enter n as integer number of intervals, a as starting point, and b as ending point in the form (n,a,b):" )
    n = input("Values n: ")
    a = float(input("Starting at a: "))
    b = float(input("Ending at b: "))
    print("For loop style")
    print(coord_for(n,a,b))
    print("While loop style")
    print(coord_while(n,a,b))
    print("List comprehension style")
    print(coord_comp(n,a,b))

