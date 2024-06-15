def search(ls):
    ls1=[]
    for i in ls:
        if ls.count(i) > len(ls):
            return ls[i]
        else:
            return 'False'





nums = eval(input())
y = search(nums)
print(y)


