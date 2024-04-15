# problem: https://pl.spoj.com/problems/PP0501A/

"""
nwd(48, 100):
a=48, b=100
48%100=48
nwd(100, 48)
100%48=4
nwd(48, 4)
48%4=0
return 4


"""


def nwd(a: int, b: int):
    if b > 0:
        return nwd(b, a % b)
    return a


def splitting(x1):
    x1 = x1.split(" ")
    return int(x1[0]), int(x1[1])


def main():
    x = int(input())
    for i in range(x):
        x1 = input()
        a, b = splitting(x1)
        print(nwd(a, b))


main()
