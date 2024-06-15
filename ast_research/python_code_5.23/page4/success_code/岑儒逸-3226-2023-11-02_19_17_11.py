def search(ls):
    ls1=[]
    for i in ls:
        if len(ls)>2:
            if ls.count(i) > len(ls)//2:
                return ls[i]
            else:
                return 'False'
        else:
            return 'False'





nums = eval(input())
y = search(nums)
print(y)


