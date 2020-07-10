a, b, c = map(int, input().split())
if b<a<c or c<a<b:
    print(a)
elif a<b<c or c<b<a:
    print(b)
elif a<c<b or b<c<a:
    print(c)
elif a==b<c or a==b>c:
    print(a)
elif b==c<a or b==c>a:
    print(b)
elif c==a<b or c==a>b:
    print(c)
else:
    print(c)