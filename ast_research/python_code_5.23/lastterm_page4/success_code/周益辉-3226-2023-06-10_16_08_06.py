def search(nums):
    a=0
    for i in nums:
        if nums.count(i)>len(nums)/2:
            a=i
    if a!=0:
        return a
    if a==0:
        return 'False'





nums = eval(input())
y = search(nums)
print(y)


