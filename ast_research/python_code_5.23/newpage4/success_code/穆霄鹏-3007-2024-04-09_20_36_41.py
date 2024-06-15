lst=eval(input())
n,m=eval(input())
if n not in range(len(lst)) or m not in range(len(lst))[1,2,3,4]:
    print('error')
else:
    del lst[n:m]
    print(lst)
