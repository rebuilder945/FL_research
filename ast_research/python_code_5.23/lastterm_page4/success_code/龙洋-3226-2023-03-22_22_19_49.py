list = []
def search(nums):
    for x in nums:
        if nums.count(x)>=2:
            if not x in list:
                list.append(x)
    if list:
        return list[0]
    else:
        return "False"





nums = eval(input())
y = search(nums)
print(y)


