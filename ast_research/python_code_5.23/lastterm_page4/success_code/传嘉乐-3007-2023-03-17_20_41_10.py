lst=eval(input())
n,m=eval(input())
if n<len(lst):
    del lst[n,m-1]
    print(lst)
else:
    print('error')
