def search(nums):
    n = len(nums)
    ls=[]
    a = False
    for x in nums:
        n1=nums.count(x)
        nums.remove(x)
        if n1 >= n//2:
            a = x
            pass
            if x not in ls:
                ls.append(x)
            else:
                pass
    return a





nums = eval(input())
y = search(nums)
print(y)


