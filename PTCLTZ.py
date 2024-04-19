# problem: https://pl.spoj.com/problems/PTCLTZ/

def odd(s):
    return 3 * s + 1


def even(s):
    return s / 2


def main():
    for i in range(int(input())):
        s = int(input())
        n = 0
        while s != 1:
            s = odd(s) if s % 2 else even(s)  # if s%2 == 1: odd(s)      else: even(s)
            n += 1
        print(n)


main()
