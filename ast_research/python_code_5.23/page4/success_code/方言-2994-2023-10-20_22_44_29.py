list=input().split(',')
wo=len(list)
n,m=eval(input())
for i in range(m%(len(list))):
    list.append(list[n])
for j in range(len(list)):
    list[j]=int(list[j])
if n>wo:
    print('False')
else:
    print(list)
