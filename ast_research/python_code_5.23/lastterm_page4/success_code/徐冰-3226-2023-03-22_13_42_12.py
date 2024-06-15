def search(nums):
    ls=[]
    for x in nums:
        ls.append(nums.count(x))
    for m in ls:
        if m>len(nums)/2:
            return x
    else:
        return False





nums = eval(input())
y = search(nums)
print(y)


