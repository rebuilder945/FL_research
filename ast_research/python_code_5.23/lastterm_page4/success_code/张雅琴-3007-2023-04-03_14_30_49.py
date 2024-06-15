lst=eval(input())
n,m=eval(input())
l=len(lst)-1
lst2=[n,m]
lst2.reverse()
if n and m <=l:
    for i in lst2:
        lst.pop(i)
    print(lst)
else:
    print("error")


