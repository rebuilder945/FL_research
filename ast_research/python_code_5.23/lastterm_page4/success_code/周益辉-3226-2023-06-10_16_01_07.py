def search(nums):
    a=0
    lst1=[]
    for i in nums:
        a=nums.count(i)
        lst1.append(a)
        if a >len(nums)/2:
            return i
    if sum(lst1)==0:
        str1='False'
        return str1





nums = eval(input())
y = search(nums)
print(y)


