def search(nums):   
    search(nums).count()
    for i in search(nums).count():
        if i>1:
            return max(set(search(nums)),key(search(nums).count))
        else:
            return "Flsh"





nums = eval(input())
y = search(nums)
print(y)


