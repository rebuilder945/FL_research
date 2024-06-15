sName=input()
a=list(sName)
b=eval(input())
n=len(a)
ls=[]
for i in range(n):
    ax=a[i]
    bx=b[i]
    c=['ax',bx]
    ls.append(c)
print(ls)
