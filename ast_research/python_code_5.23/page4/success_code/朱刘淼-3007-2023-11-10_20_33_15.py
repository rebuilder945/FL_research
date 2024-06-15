list=list(eval(input()))
n,m=map(int,input().split(","))
del list[n,m]
if n<m<len(list):
    print(list)
else:
    print("error")
