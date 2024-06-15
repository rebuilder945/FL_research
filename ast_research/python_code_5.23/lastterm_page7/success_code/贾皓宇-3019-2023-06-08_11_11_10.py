a=list(input().split())
a[1]=int(a[1])
a[2]=int(a[2])
a[3]=int(a[3])
dic={}
dic[a[1]]='english'
dic[a[2]]='python'
dic[a[3]]='math'
lst=[a[1],a[2],a[3]]
lst.sort()
t=sum(lst)/len(lst)
dic2={}
dic2[name]=a[0]
dic2[lst[0]]=dic[lst[0]]
dic2[lst[1]]=dic[lst[1]]
dic2[lst[2]]=dic[lst[2]]
dic2[avg]=t
print("%s %.2f %.2f %.2f %.2f"%(dic2[name],dic2[lst[0]],dic2[lst[1]],dic2[lst[2]],dic2[avg]))
