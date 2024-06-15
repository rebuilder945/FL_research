lst=list(eval(input()))
n,m=eval(input())
if n >0 and n>=len(lst):
    print("error")
elif n<0 and abs(n)>len(lst):
    print("error")
else:
    lst1=[lst[n]]*m
    lst2=lst+lst1
    print(lst2)
