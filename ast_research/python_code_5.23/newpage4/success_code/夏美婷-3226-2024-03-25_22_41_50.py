def search(nums):
    a=len(nums)
    n=a/2
    for i in nums:
        if nums.count(i)>n:
            return i
    for i in nums:
        list1=[]
        a=nums.count(i)
        if a>n:
            list1.append(a)
            if len(list1)==0:
                return "false"





nums = eval(input())
y = search(nums)
print(y)


