lst=eval(input())
lat1=[]
for i in lst:
    if lst.count(i)==1:
        lat1.append(i)
lat1.sort(reverse=False)
if lat1==[]:
    print("False")
else:
    print(*lat1,sep=',')
