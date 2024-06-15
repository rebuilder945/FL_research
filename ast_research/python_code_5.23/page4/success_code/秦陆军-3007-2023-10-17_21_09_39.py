lst = eval(input(''))
n,m = int(input(''))
if n < 0 or m>len(lst) or n>m:
    print('Error')
else:
    del lst[n,m]
    print(lst)
