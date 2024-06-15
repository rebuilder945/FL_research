def search(num:list):
    c=len(nums)/2
    s=none
    for x in nums:
        if nums.count(x)>c:
            s=x
        if s:
            return s
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


