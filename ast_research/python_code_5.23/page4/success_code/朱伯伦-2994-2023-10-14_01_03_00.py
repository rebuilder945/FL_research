list=input().split(",")
for i in range(len(list)):
    list[i]=int(list[i])
n,m=eval(input())
if n>=len(list) or n<=-len(list):
    print("error")
else:
    listn=list[n]
    listnm=listn*m
    for i in listnm:
        list.append(i)
    print(list)
