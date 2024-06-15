def search(nums):
    for i in range(nums):
        search(nums).count()
        if i>1:
            return max(set(search(nums)),key(search(nums).count))
        else:
            return "Flsh"





nums = eval(input())
y = search(nums)
print(y)


