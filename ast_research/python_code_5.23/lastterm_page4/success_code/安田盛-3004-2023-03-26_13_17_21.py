lst=eval(input())
a=[]
for i in lst:
    for x in range(2,i):
        if i%x==0:
            lst.remove(i)
for x in lst:
    a.append(x)
print(a)
        
