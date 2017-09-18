#!/usr/bin/env python
                                                      ### Don't forget to specify "python3" explicitly.

def fibs(n):
    fiblist = [1,1]
    if n==1:
        return [1]
    elif n==2:
        return [1,1]
    elif n>=3:
        for i in range(2,n):
            fiblist.append(fiblist[i-2]+fiblist[i-1])
        return fiblist
    else:
        print("Oopsies! not a valid input")            ### Danger! Return consistent types. Better to throw an exception than print an error.

def fib_generator():
    a = 1
    b = 1
    while True:
        yield a
        a,b = b,a+b

if __name__ == "__main__":
    n = input("Enter a value for n: ")                 ### Never use input(). Use command-line arguments, or use an interactive notebook.
    print("Fibonacci sequnce with n values")
    print(fibs(n))
    print("Fibonacci generator")
    g = fib_generator()
    fiblist = [next(g) for _ in range(n)]
    print(fiblist)
