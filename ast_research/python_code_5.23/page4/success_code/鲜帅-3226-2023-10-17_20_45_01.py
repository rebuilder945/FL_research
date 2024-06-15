ls = []
def search(a):
    for x in a:
        ls.append(a.count(x))
        b = max(a)
    if b > len(a)//2:
        a = max(a,key = a.count)
        return(a)
    else:
        return("False")





nums = eval(input())
y = search(nums)
print(y)


