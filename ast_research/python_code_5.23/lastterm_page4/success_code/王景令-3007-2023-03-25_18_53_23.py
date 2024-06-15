lst = eval(input())
lst2 = lst.copy()
a,b = eval(input())
n,m = min(a,b),max(a,b)
if m > len(lst):
    print("error")
else:
    for i in lst[n:m]:
        lst2.remove(i)
    print(lst2)




