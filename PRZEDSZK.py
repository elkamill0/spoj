# problem: https://pl.spoj.com/problems/PRZEDSZK/


def splitting(x1):
    x1 = x1.split(" ")
    return int(x1[0]), int(x1[1])


def nww(a, b):
    a1 = a
    b1 = b
    while a != b:
        if a > b:
            b += b1
        else:
            a += a1
    return a


def main():
    x = int(input())
    for i in range(x):
        x1 = input()
        a, b = splitting(x1)
        print(nww(a, b))


main()
