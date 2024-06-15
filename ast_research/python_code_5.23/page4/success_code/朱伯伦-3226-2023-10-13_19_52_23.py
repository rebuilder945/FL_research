def search(list):
    for x in list:
        num=list.count(x)
        if num>len(list)//2:
            a=x
        else:
            continue
    b=list.index(a)
    if b==0:
        return False
    else:
        return a





nums = eval(input())
y = search(nums)
print(y)


