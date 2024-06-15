a=input().split()
b=["name","english","python","math"]
dic={}
for i in range(len(a)):
    dic[b[i]]=a[i]
s=list(map(eval,a[1::]))
dic["avg"]=sum(s)/len(s)
lst=list(dic.values())
lst1=list(map(eval,lst[1:-1]))
lst1.sort(reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(lst[0],lst1[0],lst1[1],lst1[2],lst[-1]))


