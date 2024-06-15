lst=eval(input())
n,m=eval(input())

if n<0 or m<0 or n>=len(lst) or m>=len(lst):
    print("error")
else:
    del lst[n:m]
    print(lst)
