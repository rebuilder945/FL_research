lst=eval(input())
n,m=eval(input())
if n<m<len(lst):
    l1=lst[:n]
    l2=lst[m:]
    print(l1+l2)
elif n>m or len(lst)<n<m:
    print("error")
