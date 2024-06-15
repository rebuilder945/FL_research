lst=input()
n,m=eval(input())
if m<=len(lst):
    for i in range(n,m):
        lst.remove(lst[i])
    print(lst)
else:
    print('error')


