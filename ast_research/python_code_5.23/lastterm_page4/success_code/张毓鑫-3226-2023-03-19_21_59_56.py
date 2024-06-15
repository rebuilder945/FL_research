def search(a):
    b=len(a)//2
    for i in a:
        for i in a:
            a.remove(i)
            if i not in a:
                break
            if len(a)<=b:
                return i
            else:
                return False





nums = eval(input())
y = search(nums)
print(y)


