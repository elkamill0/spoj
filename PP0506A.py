# problem: https://pl.spoj.com/problems/PP0506A/


def pitagoras(x, y):
    return pow((x * x + y * y), 1 / 2)


def main():
    x = int(input())
    for i in range(x):
        tab = []
        y = int(input())
        for j in range(y):
            x1 = input().split(" ")
            x1.append(pitagoras(int(x1[1]), int(x1[2])))
            tab.append(x1)

        s = sorted(tab, key=lambda x: x[3])
        for row in s:
            print(" ".join(map(str, row[:3])))
        input()


main()
