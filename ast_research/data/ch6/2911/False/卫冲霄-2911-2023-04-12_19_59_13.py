a=input()
ls=[]
for i in range(len(a)-1,-1,-1):
    s=str((int(a[i])+5)%10)
    ls.append(s)
    b="".join(ls)
print(int(b))
