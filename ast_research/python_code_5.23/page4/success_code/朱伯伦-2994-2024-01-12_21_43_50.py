list=input().split(",")
for i in range(len(list)):
    list[i]=int(list[i])
n,m=eval(input())
if abs(n)>=len(list):
    print("error")
else:
    selected=list[n]
    for i in range(m):
        list.append(selected)
    print(list)
