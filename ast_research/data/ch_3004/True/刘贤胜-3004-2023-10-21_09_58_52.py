n1=eval(input())
n2=[]
for x in n1:
    if x>=2:
        for y in range(2,x,1):
            if x%y==0:
                break
        else:
            n2.append(x)
print(n2)
