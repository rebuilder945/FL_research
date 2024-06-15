n=list(input())
lat=[]
for x in n:
    b=(int(x)+5)%10
    lat.append(b)


for i in range(len(lat)//2):
    lat[i],lat[len(lat)-1-i]=lat[len(lat)-1-i],lat[i]
print(*lat,sep='')
