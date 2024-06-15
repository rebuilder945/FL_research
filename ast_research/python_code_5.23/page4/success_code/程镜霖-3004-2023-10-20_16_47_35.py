x1=eval(input())
x2=max(x1)
x3=[]
for i in x1:
    for x in range(2,x1):
        if i%x!=0:
            x3.append(i)
print(x3)
        


