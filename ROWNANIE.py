# problem: https://pl.spoj.com/problems/ROWNANIE/


def main():
    tab = []
    for _ in range(int(input())):
        a, b, c = map(float, input().split())
        delta = b * b - 4 * a * c
        if delta > 0:
            tab.append(2)
        elif delta == 0:
            tab.append(1)
        else:
            tab.append(0)

    [print(i) for i in tab]


main()
