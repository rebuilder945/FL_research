def search(n):
    for x in range(len(n)):
        if n.count(n[x])>n//2:
            a=n[x]
    return a
        else
    return "False"






nums = eval(input())
y = search(nums)
print(y)


