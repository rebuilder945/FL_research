a=[]
def search(nums):
    for x in nums:
        n=nums.count(x)
        if n>len(nums)/2:
            h=x
            break
        else:
            h=False
    return h





nums = eval(input())
y = search(nums)
print(y)


