nums=eval(input())
b=[]
for x in nums:
    ji=0
    for i in range(1,x+1):
        if x%i==0:
            ji+=1
    if ji==2:
        b.append(x)
print(b)


