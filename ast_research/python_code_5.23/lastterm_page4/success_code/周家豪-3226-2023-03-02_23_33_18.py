def search(xxx):
    n=len(xxx)
    for i in xxx:
        if xxx.count(i)>n//2:
            return i
    return False





nums = eval(input())
y = search(nums)
print(y)


