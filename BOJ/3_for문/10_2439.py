N = int(input())

for i in range(1,N+1):
    print('{:>{}}'.format("*"*i,N))

# 추가
# n = int(input())

# for i in range(1,n+1):
#     print('{}'.format("*"*i).rjust(n))