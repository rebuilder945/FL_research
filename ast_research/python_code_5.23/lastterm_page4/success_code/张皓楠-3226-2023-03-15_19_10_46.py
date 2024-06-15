def search(a):
    b =[]
    for i in a:
        if a.count(i)>len(a)/2:
            b.append(i)
    if len(b) != 0:
        return b[0]
    else:
        return "False"





nums = eval(input())
y = search(nums)
print(y)


