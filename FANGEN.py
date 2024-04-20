# problem: https://pl.spoj.com/problems/FANGEN/


def main():
    while True:
        r = int(input())

        if r == 0:
            return 0

        tab = []
        for j in range(abs(r)):
            tab.append("*" * (j + 1) + "." * (abs(r) - j - 1) + "*" * (abs(r) - j) + "." * j)
        for j in tab[::-1]:
            tab.append(j[::-1])

        if r > 0:
            print("\n".join(tab))
        else:
            print("\n".join(tab[::-1]))


main()
