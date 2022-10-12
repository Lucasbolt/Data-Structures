#!/usr/bin/env python3
def prime_numbers(a, b):
    for num in range(a, b+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
prime_numbers(1, 100)