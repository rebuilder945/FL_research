def search(nums):
    n=len(nums)
    lis=[]
    for x in nums:
        if nums.count(x)>=n//2:
            if not x in lis:
                lis.append(x)
    if lis:
        return lis[0]
    else:
        return "False"





nums = eval(input())
y = search(nums)
print(y)


