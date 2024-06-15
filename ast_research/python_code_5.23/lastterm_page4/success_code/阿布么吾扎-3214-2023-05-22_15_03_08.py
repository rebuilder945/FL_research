lst=eval(input())
m=lst.count(0)
if m==0:
    print(lst)
else:
    while 0 in lst:
        lst.remove(0)
        for i in range(m):
            lst.insert(len(lst),0)
        print(lst)

