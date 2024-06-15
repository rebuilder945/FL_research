lst=input().split()
lst1=["name","english","python","math"]
zipped=zip(lst1,lst1)
stu=dict(zipped)
stu["avg"]=(stu["english"]+stu["python"]+stu["math"])/3
stu2=stu.pop('name')
print(stu["name"],"%.2f".join(x for x in sorted(list(stu2.values()))),stu["avg"])









            
