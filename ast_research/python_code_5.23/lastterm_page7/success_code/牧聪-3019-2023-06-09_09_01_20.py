lst=(input().split())
lst1=["name","english","python","math"]
zipped=zip(lst1,lst)
stu=dict(zipped)
stu2=stu.copy()
del stu2["name"]
avg=sum(map(float,list(stu2.values())))/3
stu3=["%.2f"%x  for x in sorted(map(float,list(stu2.values())))]
print(stu["name"]," ".join(x for x in stu3[::-1]),"%.2f"%avg)









            
