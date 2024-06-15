lst = eval(input())
n,m = input().split(',')
a=int(n)
b = int(m)
c = len(lst)
if  a>c:
    print("error")
else:
    lst1 = [lst[a]]*b
    lst +lst1
    print(lst)
