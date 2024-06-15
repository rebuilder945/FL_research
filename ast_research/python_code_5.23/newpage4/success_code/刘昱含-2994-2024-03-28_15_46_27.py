lst=list(eval(input()))
n,m=map(int,input().split(","))
if n>0 and n>len(lst):
    print("error")
elif n<0 and abs(n)>len(lst):
    print("error")
else:
    temp=[lst[n]]*m
    lst1=lst+temp
    print(lst1)
