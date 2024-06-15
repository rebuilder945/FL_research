def search(n):
    for x in n:
        if n.count(x) >len(n)//2:
            d=x
            break
        else:
            d='False'
    return(d)





nums = eval(input())
y = search(nums)
print(y)


