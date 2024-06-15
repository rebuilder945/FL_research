def search(ls):
    ls1=[]
    for i in ls:
        if ls.count(i) not in ls1:
            ls1.append(ls.count(i))
    if max(ls1) > len(ls)//2:
        return(max(ls1))
    else:
        return 'False'





nums = eval(input())
y = search(nums)
print(y)


