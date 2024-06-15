nums=eval(input())
n=[]
for i in nums:
    if i>=2:
        for j in range(2,i,1):
            if i%j==0:
                break
        else:
            n.append(i)
print(n)
