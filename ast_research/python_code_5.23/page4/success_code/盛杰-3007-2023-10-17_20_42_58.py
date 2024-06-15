lst=eval(input())
n,m=eval(input())
lst1=lst.copy()
if n<len(lst) and m<len(lst):
    for i in range(n,m):
        lst.pop(i)
        lst1=lst
    print(lst1)
else:
    print("error")
