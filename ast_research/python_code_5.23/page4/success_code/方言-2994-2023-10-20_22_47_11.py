list=input().split(',')
wo=len(list)
n,m=eval(input())
Wind=list[n]
for i in range(m%wo):
    list.append(Wind)
for j in range(len(list)):
    list[j]=int(list[j])
if n>wo:
    print('False')
else:
    print(list)
