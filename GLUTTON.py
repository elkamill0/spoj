# problem: https://pl.spoj.com/problems/GLUTTON/

import math


def main():
    x = int(input())
    for i in range(x):
        x1 = input()
        persons, packages = map(int, x1.split())
        result = 0
        for j in range(persons):
            time = int(input())
            result += 86400//time
        print(math.ceil(result/packages))


main()

