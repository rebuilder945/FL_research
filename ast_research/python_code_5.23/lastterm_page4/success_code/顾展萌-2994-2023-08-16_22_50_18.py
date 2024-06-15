lst = eval(input())
lst1 = list(lst)

n,m = input().split(',')
a=int(n)
b = int(m)
c = len(lst)
if  a>c:
    print("error")
else:
    lst2 = [lst[a]]*b
    lst1.extend(lst2)
    print(lst1)
