def search(a):
    b=len(a)//2
    for i in a:
        while i in a:
            a.remove(i)
        if len(a)<b:
            return i
        if len(a)>=b:
            return False





nums = eval(input())
y = search(nums)
print(y)


