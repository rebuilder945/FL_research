def search(a):
    c=len(a)
    b=len(a)//2
    for i in a:
        while i in a:
            a.remove(i)
            if c-len(a)>b:
                return i
            else:
                return False





nums = eval(input())
y = search(nums)
print(y)


