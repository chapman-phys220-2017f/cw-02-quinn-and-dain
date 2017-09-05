#!/usr/bin/env python

def fibs(n):
    fiblist = [1,1]
    if n==1:
        return [1]
    elif n==2:
        return [1,1]
    elif n>=3:
        for i in range(n-2):
            fiblist.append(fiblist[n-2]+fiblist[n-1])
        return fiblist
    else:
        print("Oopsies! not a valid input")

def fib_generator():
    

if __name__ == "__main__":
    n = input("Enter a value for n: ")
    print("Fibonacci sequnce with n values")
    print(fibs(n))
