st = input()
li = []
while st != 'q' :
    li.append(st)
    st = input()
stqlnc = []
stlnc = []
for i in li :
    if not i in stlnc:
        stlnc.append(i)
        stqlnc.append(li.count(i))
std = dict(zip(stlnc,stqlnc))
stk = list(std.keys())
stk.sort()
stq = []
for j in stk:
    stq.append(std.get(j))
for k in range(len(stq)):
    if li.count(stk[k]) == max(stq):
        print('%s %d'%(stk[k],stq[k]))
    
