#!/usr/bin/env python

def compute_sum(tol=1e-2):
    k=float(1)
    sum = 0 
    while ((1/k/k)>=tol):
        sum+=(1/k/k)
        k+=1
    return sum
if __name__ == "__main__":
    print("Computing sum of infinite series:")
    print(compute_sum())
    print("With tol=1e-5:")
    print(compute_sum(1e-5))
    print("With tol=1e-10:")
    print(compute_sum(1e-10))
        
