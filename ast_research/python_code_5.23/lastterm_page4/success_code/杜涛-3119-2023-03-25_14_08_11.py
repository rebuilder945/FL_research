a=eval(input())
b=a.reverse()
c=[]
for i in a:
    if i not in c:
        c.insert(0,i)
print(c)
