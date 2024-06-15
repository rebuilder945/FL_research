def search(a):
    b=len(a)//2
    c=len(a)%2
    for i in a:
        while i in a:
            a.remove(i)
        if c==0 and len(a)<b:
            return i
        elif c!=0 and len(a)<=b:
            return i
        elif len(a)>=b:
            return False





nums = eval(input())
y = search(nums)
print(y)


