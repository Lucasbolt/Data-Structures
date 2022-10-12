#!/usr/bin/env python3

def prefix_average(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
      total+= S[j]
      A[j] = total/(j+1)
    return A
a = [1, 5, 4, 6, 7, 8]
b = prefix_average(a)
print(b[1], b[2])