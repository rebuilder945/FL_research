def search(ls):
    n = len(ls)
    for i in ls:
        if ls.count(i)>n/2:
            print(ls[i])
        else:
               print(False)     


    






nums = eval(input())
y = search(nums)
print(y)


