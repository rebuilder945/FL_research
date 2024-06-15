def search(ls):
    ls1=[]
    for i in ls:
        if ls.count(i) not in ls1:
            ls1.append(ls.count(i))
    return max(ls1)





nums = eval(input())
y = search(nums)
print(y)


