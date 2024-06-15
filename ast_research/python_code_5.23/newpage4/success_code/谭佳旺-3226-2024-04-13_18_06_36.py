def search(a):
    b=[]
    for i in a:
        if a.count(i)>1:
            b.append(i)
            return b
        if a.count(i)==1:
            print("False")





nums = eval(input())
y = search(nums)
print(y)


