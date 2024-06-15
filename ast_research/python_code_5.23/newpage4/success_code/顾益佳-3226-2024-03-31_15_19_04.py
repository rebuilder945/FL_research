def search(nums):
    lst = []
    a = 0
    for x in nums:
        a = 0
        for i in nums:
            if x == i :
                a += 1
        if a >= len(nums)//2:
            lst.append(x)
    if lst ==[] :
        return "False"
    else:
        return lst[0]
       





nums = eval(input())
y = search(nums)
print(y)


