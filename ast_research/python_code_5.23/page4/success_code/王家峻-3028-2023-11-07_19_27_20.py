a,b,c=eval(input())
lst=[]
lst.append(a)
for i in range(b-1):
    t=a+c
    a=t
    lst.append(t)
print(lst)
