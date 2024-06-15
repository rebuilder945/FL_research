names=input().split(',')
nums=eval(input().split(','))
n=len(nums)
lst=[]
for i in range(n):
    lst.append([names[i],nums[i]])
print(lst)
