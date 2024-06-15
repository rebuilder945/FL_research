n=input()
x={}
while n!='q':
    if n not in x:
         x[n]=1
    else:
        x[n]+=1
    n=input()
m=max(x.value())
print(m)
