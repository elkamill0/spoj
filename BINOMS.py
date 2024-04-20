# problem: https://pl.spoj.com/problems/BINOMS/

import math


def silnia(x):
    return math.factorial(x)


def main():
    for i in range(int(input())):
        n, k = map(int, input().split())
        print(int(silnia(n) / (silnia(k) * (silnia(n - k)))))


main()
