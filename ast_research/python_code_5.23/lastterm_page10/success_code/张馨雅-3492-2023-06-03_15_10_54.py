s=list(input())
w=[]
for i in s:
    if s.count(i)!=1:
        pass
    else:
        w.append(i)
if w:
    print(w[0])
else:
    print('None')
