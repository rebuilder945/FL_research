a=eval(input())
nums=[]
k=len(a)
for i in a[0:k+1]:
    if i<2:
         continue
    for d in range(2,i):
        if i%d==0:
            break
        else:
           nums.append(i)
print(nums)
