lst=list(map(int,input().split(',')))
n,m=map(int,input().split(','))
if n <= len(lst):
    del lst[n:m]
    print(lst)
else:
    print("error")
