lst=eval(input())
lat1=[]
for i in lst:
    if lst.count(i)==1:
        lat1.append(i)
if lat1==[]:
    print("False")
else:
    print(*lat1,sep=',')
