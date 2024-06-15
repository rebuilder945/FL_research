a=eval(input())
b=[]
for x in a:
    yes=1
    for i in range(2,x):
        if x%i==0:
            yes=0
            break
    if yes and x!=1:
        b.append(x)
print(b) 
