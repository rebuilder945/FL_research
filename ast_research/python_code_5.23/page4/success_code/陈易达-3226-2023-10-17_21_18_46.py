def search(ls):
    n = len(ls)
    for x in ls:
        if ls.count(x) > n//2:
            return x
            break
        else:
            print(False)





nums = eval(input())
y = search(nums)
print(y)


