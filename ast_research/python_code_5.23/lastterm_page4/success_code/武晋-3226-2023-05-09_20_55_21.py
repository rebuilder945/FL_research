def search(y):
    for i in y:
        if (y.count(i))>(len(y)//2):
            return i
    return False
             





nums = eval(input())
y = search(nums)
print(y)


