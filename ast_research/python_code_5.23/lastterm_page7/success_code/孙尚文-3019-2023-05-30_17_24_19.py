a=input().split()
dic={}
dic["name"]=a[0]
dic["english"]=a[1]
dic["python"]=a[2]
dic["math"]=a[3]

avg=(int(a[1])+int(a[2])+int(a[3]))/3
chengji=[]
chengji.append(int(a[1]))
chengji.append(int(a[2]))
chengji.append(int(a[3]))
chengji.sort(reverse=True)

suoyou=[a[0]]
for i in chengji:
    suoyou.append(str(i))

print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(a[0],chengji[0],chengji[1],chengji[2],avg))
