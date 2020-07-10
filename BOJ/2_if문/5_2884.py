h, m = map(int, input().split())
hm = h*60 + m
if hm < 45:
    hm = 24*60 + hm
alarm = hm-45
alarmh = alarm//60
alarmm = alarm%60
print(alarmh, alarmm)

# 추가
# h, m = map(int, input().split())

# if m >= 45:
#     print(h, m-45)
# else:
#     if h == 0:
#         h = 24
#     print(h-1, m+60-45)