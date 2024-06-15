lst = eval(input())
n,m = input()
a = len(lst)
if n <= a+1 and m <= a+1:
    del  lst[n,m,1]
else:
    print('error')

