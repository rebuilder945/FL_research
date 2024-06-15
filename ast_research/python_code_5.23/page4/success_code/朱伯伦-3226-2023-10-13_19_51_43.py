def search(list):
    for x in list:
        num=list.count(x)
        if num>len(list)//2:
            a=x
        else:
            continue
    b=list.index(a)
    if b==0:
        print(False)
    else:
        print(a)





nums = eval(input())
y = search(nums)
print(y)


