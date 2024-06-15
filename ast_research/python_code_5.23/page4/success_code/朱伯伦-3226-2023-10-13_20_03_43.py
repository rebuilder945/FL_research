def search(list):
    for x in list:
        n=list.count(x)
        if n>len(list)//2:
            a=x
        else:
            continue
    b=list.index(a)
    if b==False:
        return False
    else:
        return a
nums  =  eval(input())
y  =  search(nums)
print(y)





nums = eval(input())
y = search(nums)
print(y)


