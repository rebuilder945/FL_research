def search(n):
    n=list(n)
    for x in n:
        a=n.count(x)
        if a>len(n)//2:
            return(x)
        else:
            return("False")





nums = eval(input())
y = search(nums)
print(y)


