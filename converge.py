#!/usr/bin/env python

def compute_sum(tol=1e-2):
    k=1
    sum = 0 
    while (1/k**2)>=tol:
        sum+=(1/k**2)
        k+=1
    return sum
if __name__ == "__main__":
    print("Computing sum of infinite series:")
    print(compute_sum())
    print("With tol=1e-10:")
    print(compute_sum(1e-10))
    print("With tol=1e-100:")
    print(compute_sum(1e-100))
        
