def search(SB):
    n = len(SB)
    for x in SB:
        if SB.count(x) > n//2:
            return(x)
        else:
            return(False)





nums = eval(input())
y = search(nums)
print(y)


