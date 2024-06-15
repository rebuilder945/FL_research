def search(ls):
    n = len(ls)
    if ls.count(x) > n//2 for x in ls:
        for x in ls:
            if ls.count(x) > n//2:
                return x
    else:
        print(False)
    
 





nums = eval(input())
y = search(nums)
print(y)


