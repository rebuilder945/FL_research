def search(nums):
    c=len(nums)/2
    for x in nums:
        a=[nums.count(x)]
        b=max(a)
        if b>c:
            for i in nums:
                if nums.count(i)==b
                     return i

        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


