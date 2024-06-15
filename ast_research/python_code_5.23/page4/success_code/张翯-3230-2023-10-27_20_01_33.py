lst=eval(input())
lst.sort()
lst.reverse()
if lst[0]==0:
    print("0")
else:
    lst2=[str(i) for i in lst]
    num=''.join(lst2)
    print(num)
