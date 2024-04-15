# problem: https://pl.spoj.com/problems/PP0502B/


def splitting(x1):
    x1 = x1.split(" ")
    return x1[1:]


def main():
    x = int(input())
    for i in range(x):
        x1 = input()
        print(" ".join(splitting(x1)[::-1]))


main()