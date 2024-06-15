a=eval(input())
c=[]
for x in a:
    for i in range(2,10):
        if x%i==0 or x==1:
            a.remove(x)
        else:
            c.append(x)
print(c)



