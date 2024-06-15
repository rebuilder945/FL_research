lst=eval(input())
n,m=eval(input())
if n>=len(lst) or m>=len(lst):
    print("error")
else:
    lst1=lst[:n]+lst[m:]
    print(lst1)
