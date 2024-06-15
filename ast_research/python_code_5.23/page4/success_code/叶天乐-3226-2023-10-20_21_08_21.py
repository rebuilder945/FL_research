def search(nums):
    ls = [nums]
    for x in ls:
        if count(x)>len(ls):
            print(x)
        else:
            print(False)





nums = eval(input())
y = search(nums)
print(y)


