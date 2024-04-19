# problem: https://pl.spoj.com/problems/SKARBFI/

def back_road(step):
    if step[0] > 0:
        print(0, step[0])
    elif step[0] < 0:
        print(1, step[0] * -1)
    if step[1] > 0:
        print(3, step[1])
    elif step[1] < 0:
        print(2, step[1] * -1)



def main():
    for i in range(int(input())):
        step = [0, 0]
        for j in range(int(input())):
            a, b = map(int, input().split())
            if a == 0:
                step[0] += b
            elif a == 1:
                step[0] -= b
            elif a == 2:
                step[1] -= b
            elif a == 3:
                step[1] += b
        if step == [0, 0]:
            print("studnia")
        else:
            back_road(step)


main()
