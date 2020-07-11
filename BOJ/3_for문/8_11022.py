import sys

T = int(input())

x = 0
for i in range(T):
    x += 1
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(x,a,b,a+b))

# 추가
# t = int(input())

# for i in range(1,t+1):
#     a, b = map(int, input().split())
#     print("Case #{}: {} + {} = {}".format(i,a,b,a+b))