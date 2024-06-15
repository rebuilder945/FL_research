n=input()
m=[s for s in n]
q=[m.count(g) for g in m]
if min(q)>1:
    print('None')
for i in n:
    if m.count(i)==1:
        print(i)
        break

