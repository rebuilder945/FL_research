def search(n):
    l=len(n)
    x=round(l/2)    
    for i in n:
        c=n.count(i)
        if c>=x:
            return i
  






nums = eval(input())
y = search(nums)
print(y)


