def search(a):
    d=''
    for i in a:
        if len(i)>len(a)//2:
        d+=i
    return d[0]






nums = eval(input())
y = search(nums)
print(y)


