# problem: https://pl.spoj.com/problems/FLAMASTE/


def itering(w):
    w += " "
    i = 1
    combo = 1
    word = ""
    while i < len(w):
        if w[i - 1] == w[i]:
            combo += 1
        else:
            if combo <= 2:
                for c in range(combo):
                    word += w[i - 1]
            else:
                word += w[i - 1] + str(combo)
            combo = 1
        i += 1
    return word


def main():
    x = int(input())
    for i in range(x):
        x1 = input()
        print(itering(x1))


main()
