def search(nums):
    n=len(nums)
    ls=[]
    for i in nums:
        if nums.count(i) >(n//2):
            ls.append(nums.count(i))
            return max(ls)
        else:
            return False
        
    





nums = eval(input())
y = search(nums)
print(y)


