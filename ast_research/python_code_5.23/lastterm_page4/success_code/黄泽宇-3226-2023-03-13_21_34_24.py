def search(u):
    b=len(u)
    for x in u:
        if u.count(x) > b/2:
            return(x)
    else:
        return("False")






nums = eval(input())
y = search(nums)
print(y)


