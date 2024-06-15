def search(u):
    u=list(nums)
    b=len(u)
    for x in u:
        if u.count(x) > b:
            return(x)
    else:
        return("False")





nums = eval(input())
y = search(nums)
print(y)


