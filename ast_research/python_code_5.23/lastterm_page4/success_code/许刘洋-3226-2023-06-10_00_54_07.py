def search(a):
    b=[]
    for i in a:
        if a.count(i)>len(a)//2:
            return i 
            b.append(i)
    if b==[]:      
        return False






nums = eval(input())
y = search(nums)
print(y)


