def search(lst):
    lstR=[x for x in lst if lst.count(x)>len(lst)//2]
    return lstR[0] if lstR else False






nums = eval(input())
y = search(nums)
print(y)


