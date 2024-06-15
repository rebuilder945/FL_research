def search(L=[]):
    for i in L:
        if L.count(i)>len(L)//2:
            return i
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


