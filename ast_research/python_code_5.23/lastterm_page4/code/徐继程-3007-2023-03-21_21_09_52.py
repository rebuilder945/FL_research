lst=input()
n,m=eval(input())

if n>m or m>=len(lst):
    print('error')
else:
    lst.pop(n:m)
    print(lst)

