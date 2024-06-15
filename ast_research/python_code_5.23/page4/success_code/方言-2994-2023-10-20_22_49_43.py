list=input().split(',')
wo=len(list)
n,m=eval(input())
if n<=wo:
    wind=list[n]
    for i in range(m%wo):
        list.append(wind)
    for j in range(len(list)):
        list[j]=int(list[j])
if n>wo:
    print('False')
else:
    print(list)
