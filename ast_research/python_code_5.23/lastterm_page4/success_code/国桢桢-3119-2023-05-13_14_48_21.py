l = eval(input())
l1=[]
for i in range(0,-1,-1):
    if l.count(l[i])>1 and not l[i] in l1:
        l1.append(l[i])
l1.reverse()
print(l1)       
