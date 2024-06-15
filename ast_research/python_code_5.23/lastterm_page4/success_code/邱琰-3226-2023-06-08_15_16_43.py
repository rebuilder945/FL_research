def search(nums):
    n=len(nums)
    ls=[]
    for i in nums:
        if nums.count(i) >(n//2):
            return i
        else:
            return False
        
    





nums = eval(input())
y = search(nums)
print(y)


