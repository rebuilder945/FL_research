lst=input()
n,m=input().split('','')
n=int()
m=int()
if n<len(lst) and m<len(lst):
    if n<m:
       del lst[n:m]
       print(lst)
else:
    print("error")

