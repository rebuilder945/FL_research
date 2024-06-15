lst=list(eval(input()))
n,m=eval(input())
if n>len(lst) or n<1:
    print("error")
else:
    temp=str(lst[n])*m
    temp1=list(map(int,temp))
    lst1=lst+temp1
    print(lst1)
