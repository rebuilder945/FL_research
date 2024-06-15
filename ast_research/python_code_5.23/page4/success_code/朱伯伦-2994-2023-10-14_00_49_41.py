list=input().split(",")
n,m=eval(input())
listn=list[n]
if n>=len(list) or n<=-len(list):
    print("error")
else:
    list=list.extend(listn*m)
    print(list)
