def search(nums):
    a= max(set(nums), key=nums.count)
    d=int(nums.count(a))
    b=int(len(nums))
    c=b//2

    if d >c:
        return a
    else:
        b="False"
        return b






nums = eval(input())
y = search(nums)
print(y)


