def search(n):
    n=list(n)
    n.sort()
    return(n[int(len(n))//2])





nums = eval(input())
y = search(nums)
print(y)


