
lst = eval(input())
n,m = map(int,input().split(','))
if n>=0 and m>=0 and m <= len(lst) and n<=len(lst):
    del lst[n:m]
    print(lst) 
else:
    print('error')

