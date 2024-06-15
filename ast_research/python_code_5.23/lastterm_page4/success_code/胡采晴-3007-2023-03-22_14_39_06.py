lst = input()
(n,m) = eval(input())
s = len(lst)
if n <= 0 or m>s:
    print('error')
else:
    lst.remove(lst[n,m-1])
    print(lst)

