lst = eval(input(''))
n, m = eval(input(''))
n = int(n)
m = int(m)
if m > len(lst)-1 or  n > len(lst)-1:
    print('error')
else:
   lst[n:m]
   print(lst)

