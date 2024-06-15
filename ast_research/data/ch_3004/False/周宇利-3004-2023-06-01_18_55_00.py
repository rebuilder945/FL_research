a=eval(input())
b=[]
for x in a:
    i=0
    for y in range(2,x):
        if x%y!=0:
            i=i+1
        if i==x-2:
            b.append(x)
print(b)
