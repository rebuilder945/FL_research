a=eval(input())
c=str(a)
b=list(c)
lst=[]
for i in b:
    d=int(i)
    e=(d+5)%10
    f=str(e)
    lst.append(f)
lst.reverse()

print("".join(j for j in lst))


