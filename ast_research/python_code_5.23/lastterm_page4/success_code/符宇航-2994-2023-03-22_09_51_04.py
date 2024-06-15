lst = list(eval(input()))
n,m = input().split(',')
n = int(n)
m = int(m)
a = len(lst)
b = a-2*a
if n<b or n>a:
    print('error')
else:
    qq = lst[n]
    lst1 = [qq]*m
    lst2 = lst + lst1
    print(lst2)

   
    

