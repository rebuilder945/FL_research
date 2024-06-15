n=input()
p=[]
for i in n:
    s=str((int(i)+5)%10)
    p.append(s)
p.reverse()
m="".join(p)
print(m)
