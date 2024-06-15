a=eval(input())
nums=[]
for i in a[0,len(a)]:
    for d in range(0,i):
        if i%d==0:
           nums.append(i)
print(nums)
