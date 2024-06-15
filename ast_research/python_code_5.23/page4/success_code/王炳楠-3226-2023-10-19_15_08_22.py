def search(lie):
    n=len(lie)
    ls1=[]
    for i in lie[::1]:
        c=1
        if i in lie:
            lie.remove(i)
        while i in lie:
            lie.remove(i)
            c=c+1
        if c>n/2:
            ls1.append(i)
    return ls1[0]






nums = eval(input())
y = search(nums)
print(y)


