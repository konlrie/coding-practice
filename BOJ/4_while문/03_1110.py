N = int(input())

a = N
cycle = 0

while True:
    if a < 10:
        a = str(0) + str(a)
        a = str(a)
        c = str(int(a[0])+int(a[1]))
        a = str(a[-1]) + str(c[-1])
        a = int(a)
        cycle += 1
    else:
        a = str(a)
        c = str(int(a[0])+int(a[1]))
        a = str(a[-1]) + str(c[-1])
        a = int(a)
        cycle += 1

    if a == N:
        break
    else:
        pass

print(cycle)