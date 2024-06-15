st = list(input())
mx = 0
now = 0
ans = []
pre = []
for x in st:
    if x.isdigit():
        now += 1
        pre.append(x)
    else:
        if now == 0:
            continue
        else:
            if now >= mx:
                ans = pre
                mx = now
            pre = []
            now = 0
if now >= mx:
    ans = pre
    mx = now
if mx != 0:
    print("".join (x for x in ans))
else:
    print("No digits")

