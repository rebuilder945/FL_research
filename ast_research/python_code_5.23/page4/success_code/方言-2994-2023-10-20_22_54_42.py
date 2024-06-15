list=input().split(',')
wo=len(list)
n,m=eval(input())
print(m)
if n<=wo:
    wind=list[n]
    if m>wo:
        for i in range(m):
            list.append(wind)
    else:        
        for i in range(m%wo):
            list.append(wind)
    for j in range(len(list)):
        list[j]=int(list[j])
if n>wo:
    print('error')
else:
    print(list)
