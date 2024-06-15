lst = eval(input())
lst.sort()
for i in lst:
    if lst.count(i) == 1:
        print(i,end=",")
    else:
        pass
