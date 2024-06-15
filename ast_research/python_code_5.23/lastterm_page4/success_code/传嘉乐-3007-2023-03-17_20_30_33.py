lst=list(eval(input))
n,m=eval(input())
if n<len(list):
    del lst[n,m-1]
    print(lst)
else:
    print('error')
