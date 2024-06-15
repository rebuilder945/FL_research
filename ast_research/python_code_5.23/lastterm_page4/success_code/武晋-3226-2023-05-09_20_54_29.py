def search(y):
    for i in y:
        s=0
        if (y.counts(i))>(len(y)//2):
            return i
    return False
             





nums = eval(input())
y = search(nums)
print(y)


