list=input().split(",")
n,m=eval(input())
if n>=len(list) or n<=-len(list):
    print("error")
else:
    listn=list[n-1]
    listnm=listn*m
    list=list.extend(listnm)
    print(list)
