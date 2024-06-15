list=input().split(',')
n,m=eval(input())
for i in range(m):
    list.append(list[n])
for j in range(len(list)):
    list[j]=int(list[j])
print(list)
