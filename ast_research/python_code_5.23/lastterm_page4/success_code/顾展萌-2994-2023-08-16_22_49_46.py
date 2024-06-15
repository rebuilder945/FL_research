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
  
    print(lst1)
