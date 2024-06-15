lst = eval(input())
n,m = input().split(',')
a=int(n)
b = int(m)
c = len(lst)
if a <0 or a>c:
    print("error")
else:
    lst1 = [lst[a]]*b
    lst1.extend(lst)
    print(lst)
