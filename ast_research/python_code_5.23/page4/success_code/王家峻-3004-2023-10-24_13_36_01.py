n=eval(input())
for i in n:
    c=[]
    c.append(i)
    for x in range(2,i//2):
        if i % x==0:
            c.remove(i)
print(c)
