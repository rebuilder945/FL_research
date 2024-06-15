def search(nums):
    n=len(nums)
    for x in nums:
        nums.count(x)
        if nums.count(x)> (n//2):
            return(x)
        if  nums.count(x)<= (n//2):
            return(False)






nums = eval(input())
y = search(nums)
print(y)


