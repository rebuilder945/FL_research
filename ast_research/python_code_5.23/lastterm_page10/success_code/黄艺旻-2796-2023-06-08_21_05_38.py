a=input()
t=[]
l=[]
for x in a:
    if x.isdigit():
        t.append(x)
        if len(t)>=len(l):
            l=t.copy()
    else:
        t=[]
if len(l)>0:
    print(''.join(l))
else:
    print('No digits')
