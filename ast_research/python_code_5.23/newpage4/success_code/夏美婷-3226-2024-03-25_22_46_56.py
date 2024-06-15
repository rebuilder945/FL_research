def search(nums):
    a=len(nums)
    n=a/2
    for i in nums:
        list1=[]
        a=nums.count(i)
        if a>n:
            list1.append(i)
    if len(list1)==0:
        return "false"
    else:
        return list1[0]





nums = eval(input())
y = search(nums)
print(y)


