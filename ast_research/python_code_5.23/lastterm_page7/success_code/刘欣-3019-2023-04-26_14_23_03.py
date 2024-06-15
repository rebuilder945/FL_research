lis1=input().split()
lis2=["name","english","python","math"]
dic=dict(zip(lis1,lis2))
average=float(dic["english"]+dic["python"]+dic["math"])/3
dic["ave"]=average
print(dic["name"],end=" ")
for i in sorted([dic["english"],dic["python"],dic["math"]],reverse=True):
    print("%.2f"%i,end=" ")
print(dic["ave"])
