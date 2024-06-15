a=eval(input())
b=[]
n=1
for x in a:
    for i in range(x-1):
        n+=1
        if x//n:
            b.append(x)
print(b)
        
