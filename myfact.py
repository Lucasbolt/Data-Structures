#!/usr/bin/python3
#this is a factorial function!
import sys

def Killo(n):
    if n==0: return 1
    return n*Killo(n-1)
  

if __name__ == "__main__":
    n = int(input("Enter n: "))
    n = Killo(n)
    print(n)