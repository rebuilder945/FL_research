a=eval(input())
b=[]
for x in a:
    for i in range(2,x):
        if  x%i==0:
            break
    else: 
        b.append(x)   
print(b)
#因为2已经在a里了所以（2，x）是取不到数的
