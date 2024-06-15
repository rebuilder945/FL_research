name,english,python,math=input().split()
stu={}
stu["name"]=name
stu["english"]=int(english)
stu["python"]=int(python)
stu["math"]=int(math)
stu["avg"]="%.2f"%((int(english)+int(python)+int(math))/3)
chengji=sorted([stu["english"],stu["python"],stu["math"]],reverse=True)
print(stu["name"],end=" ")
for i in chengji:
    print("%.2f"%i,end=" ")
print(stu["avg"])
