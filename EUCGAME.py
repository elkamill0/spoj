# problem: https://pl.spoj.com/problems/EUCGAME/


def main():
    for i in range(int(input())):
        a, b = map(int, input().split())

        while a != b:
            if a < b:
                b -= a
            else:
                a -= b
        print(a + b)


main()
