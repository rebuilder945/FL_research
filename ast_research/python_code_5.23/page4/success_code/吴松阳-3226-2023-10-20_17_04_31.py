def search(n):
    a = max(n,key = n.count)
    mos = n.count(a)
    if mos > n/2:
        return a
    else:
        return 'False'





nums = eval(input())
y = search(nums)
print(y)


