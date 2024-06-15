names=list(input().split(','))
nums=list(eval(input()).split(','))
n=len(nums)
lst=[]
for i in range(n):
    lst.append(list(names[i],nums[i]))
lst=sorted(lst,key=lambda x:x[1])
print(lst)
