lst=eval(input())
n,m=eval(input())
if n<m and n>=0 and m<=len(lst):
    lst1=lst[:n]
    lst2=lst[m:]
    print(lst1+lst2)
else:
    print("error")

