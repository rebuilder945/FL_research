name,eg,py,ma=input().split()
dic={}
dic["english"]=int(eg)
dic["python"]=int(py)
dic["math"]=int(ma)
ave=(int(eg)+int(py)+int(ma))/3
lis=list(dic.values())
print(name,end=" ")
for i in range(1,len(lis)):
    i=int(i)
lis.sort(reverse=True)
for i in lis:
    print("%.2f"%i,end=" ")
print("%.2f"%ave)
