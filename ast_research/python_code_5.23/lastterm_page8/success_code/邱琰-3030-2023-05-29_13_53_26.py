names=input().split(',')
nums=eval(input().split(','))
n=len(nums)
lst=[]
for i in range(n):
    lst[i]=list(names[i],nums[i])
lst=lst.sort
print(lst)
