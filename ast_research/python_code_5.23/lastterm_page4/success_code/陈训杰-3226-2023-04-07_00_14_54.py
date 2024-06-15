def search(m):
    n=len(m)
    for i in m:
        if m.count(i)>n//2:
            return i
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


