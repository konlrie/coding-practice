a, b, c = map(int, input().split())
p1 = (a+b)%c
p2 = (a%c + b%c)%c
p3 = (a*b)%c
p4 = (a%c * b%c)%c
print(p1)
print(p2)
print(p3)
print(p4)