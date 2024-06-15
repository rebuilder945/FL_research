op = list(input())
st = input()
ans = []
now = []
t = 0
for s in op:
    if s == st[t]:
        t += 1
        now.append(s)
        if t == len(st):
            t = 0
            now = []
    else:
        if t != 0:
            ans = ans + now
            now = []
            t = 0
        ans.append(s)
print("".join(str(x) for x in ans))

