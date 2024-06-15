list0=input().split(',')
list1=input().split(',')
l0=[]
n=int(list1[0])
m=int(list1[1])
for i in list0:
    l0.append(int(i))
if n >= len(list0):
    print('error')
else:
    i=1
    while i<=m:
        l0.append(int(list0[n]))
        i+=1
    print(l0)
