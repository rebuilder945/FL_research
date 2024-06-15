a=eval(input())
nums=[]
i=2
for i in range(1,100000000):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        nums.append(i)
b=[]
for x in a:
    if x not in nums:
        c=0
    else:
        b.append(x)
print(b)

