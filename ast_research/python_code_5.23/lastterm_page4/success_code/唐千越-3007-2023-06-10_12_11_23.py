lst = eval(input())
n,m = eval(input())
l = len(lst)
lst1 = []
if n<=m and m<=l:
    for i in lst[0:n]:
        lst1.append(i)
    for i in lst[m:l]:
        lst1.append(i)
    print(lst1)
else:
    print("error")
