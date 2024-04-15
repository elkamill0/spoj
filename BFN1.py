# problem: https://pl.spoj.com/problems/BFN1/

'''
a = 28
28 != 82,
28 + 82 = 110

110 != 011
110 + 011 = 121

121 == 121

'''


def adding(a, iteration):
    a = int(a) + int(a[::-1])
    a = str(a)
    if a == a[::-1]:
        return a, str(iteration)
    else:
        return adding(a, iteration + 1)


def main():
    x = int(input())
    for i in range(x):
        a = input()
        if a == a[::-1]:
            print(a, 0)
        else:
            print(" ".join(adding(a, 1)))


main()
