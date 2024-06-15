list=[]
def search(nums):
    for x in nums:
        if nums.count(x)>=2:
            if not x in list:
                list.append(x)
                return x
    if not list:
        return "False"





nums = eval(input())
y = search(nums)
print(y)


