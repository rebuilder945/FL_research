lis1=input().split()
lis2=["name","english","python","math"]
dic=dict(zip(lis2,lis1))
average=(float(dic["english"])+float(dic["python"])+float(dic["math"]))/3 
dic["ave"]=average
print(dic["name"],end=" ")
for i in sorted([dic["english"],dic["python"],dic["math"]],reverse=True):
    i=float(i)
    print("%.2f"%i,end=" ")
print("%.2f"%dic["ave"])
