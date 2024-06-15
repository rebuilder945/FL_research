def  search(nums):   
    a=nums.count(max(nums,key=nums.count))
    a=2*a
    if a>len(nums):
        a=max(nums,key=nums.count)
    else:
        a=False
    return a





nums = eval(input())
y = search(nums)
print(y)


