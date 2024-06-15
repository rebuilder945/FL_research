a,b,c,d=input()
l1=eval(input())
l2=[]
l2.append(a,b,c,d)
m=[]
for i in range(len(l1)) :
    n=[]
    n.append(l2[i])
    n.append(l1[i])
    m.append(n)
print(m)
    
