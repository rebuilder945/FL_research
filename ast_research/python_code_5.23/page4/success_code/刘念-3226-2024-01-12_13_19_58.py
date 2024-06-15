def search(a):
    m=0
    for i in a:
        if a.count(i)>len(a)//2:
            m=1
            h=i
if m==1:
    print(h)
else:
    print('False')





nums = eval(input())
y = search(nums)
print(y)


