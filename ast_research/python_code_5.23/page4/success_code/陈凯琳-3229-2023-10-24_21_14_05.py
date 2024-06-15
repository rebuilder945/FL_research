lit=eval(input())
slit=list(set(lit))
s=[]
for i in range(len(slit)):
    if lit.count(slit[i])==1:
        s.append(str(slit[i]))
s.sort()
if len(s)==0:
    print('False')
else:
    print(','.join(s))
