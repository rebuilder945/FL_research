lst=input().split()
dic={}
dic["name"]=lst[0]
dic["english"]=eval(lst[1])
dic["python"]=eval(lst[2])
dic["math"]=eval(lst[3])
avg=(dic["english"]+dic["python"]+dic["math"])/3
lst2=list(map(float,lst[-1:0:-1]))
lst2.sort()
lst2.reverse()
lst2=lst2+[avg]
print("%s %.2f %.2f %.2f %.2f"%(dic["name"],lst2[0],lst2[1],lst2[2],lst2[3]))
