lst=eval(input())
n,m=eval(input())
if -len(lst)>m or n>m or n>=len(lst):
    print("error")
else:
    print(lst[:n]+lst[m:])
