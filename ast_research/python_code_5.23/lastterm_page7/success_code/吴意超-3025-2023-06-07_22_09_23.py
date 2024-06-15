a = {}
while True:
    s = input()
    if s == 'q':
        break
    if s not in a:
        a[s] = 0
    a[s] +=1

mc = 0
mw = ''
for w,c in a.items():
    if c > mc:
        mc = c
        mw = w
print(mw,mc)
