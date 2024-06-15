s=input()
ls=[]
for i in s:
    a=int(i)
    a+=5
    a=a%10
    ls.append(a)
ls.reverse()
ls1=[str(y) for y in ls]
m=''.join(ls1)
print(m)
