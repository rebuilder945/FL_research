a=eval(input())
nums=[]
k=len(a)
for i in a[0:k]:
    for d in range(0,i):
        if i%d==0:
           nums.append(i)
print(nums)
