def search(n):
    mos = n.count(max(n,key = n.count())
    if mos > n//2:
        return mos
     else:
        return 'False'





nums = eval(input())
y = search(nums)
print(y)


