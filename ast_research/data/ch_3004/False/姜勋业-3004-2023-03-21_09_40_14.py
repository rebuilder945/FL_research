a=eval(input())
nums=[]
k=len(a)
for i in a[1:k]:
    for d in range(2,i):
        if i%d==0:
            break
    else:
           nums.append(i)
print(nums)
