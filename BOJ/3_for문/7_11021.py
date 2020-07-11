import sys

T = int(input())

x = 0
for i in range(T):
    x += 1
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(x,a+b))