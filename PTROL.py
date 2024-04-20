# problem: https://pl.spoj.com/problems/PTROL/


def main():
    for i in range(int(input())):
        x = input().split(" ")
        end = int(x[1])
        x = x[2:]
        print(" ".join(x), end)


main()
