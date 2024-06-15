a=eval(input())
b=[]
for i in a:
    if i!=0:
        b.append(i)
for i in range(len(a)-len(b)):
    b.append(i*0)
print(b)        

