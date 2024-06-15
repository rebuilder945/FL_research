def search(a):
    b=[]
    for i in a:
        if a.count(i)>1:
            print(i)
        if a.count(i)==1:
            print("False")





nums = eval(input())
y = search(nums)
print(y)


