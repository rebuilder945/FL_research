def search():
    a=len(nums)
    for x in nums:
        b=nums.count(x)
        if b>=a/2:
            return x
             
    return
nums  =  eval(input())
y  =  search(nums)
print(y)
