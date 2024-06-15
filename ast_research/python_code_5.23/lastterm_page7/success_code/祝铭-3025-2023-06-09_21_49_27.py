stl = input().split(' ')
stqlnc = []
stlnc = []
for i in stl :
    if not i in stlnc:
        stlnc.append(i)
        stqlnc.append(stl.count(i))
std = dict(zip(stlnc,stqlnc))
stk = list(std.keys())
stk.sort()
stq = []
for j in stk:
    stq.append(std.get(j))
for k in range(len(stq)):
    if stl.count(stk[k]) == max(stq):
        print('%s %d'%(stk[k],stq[k]))
