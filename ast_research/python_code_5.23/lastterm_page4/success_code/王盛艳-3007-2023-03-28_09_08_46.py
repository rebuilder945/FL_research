lst = list(eval(input()))
nm = eval(input())
n = nm[0]
m = nm[1]
if n in lst:
    if m not in lst:
        print("error")
    else:
        lst2 = lst.remove(range(n,m))
        print(lst2)
else:
    print("error")
