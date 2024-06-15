def search(nums):
    a=0
    for x in nums:
        if nums.count(x)>len(nums)/2:
            a=x
    if a>0 or a<0:
        return a
    elif a==0:
        return"False"





nums = eval(input())
y = search(nums)
print(y)


