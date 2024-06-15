stu = {"name":input(),"english":eval(input()),"python":eval(input()),"math":eval(input())}

pingjun = (stu["english"] + stu["python"] + stu["math"])/3
stu["avg"] = pingjun
chengji = sorted([stu["english"],stu["python"],stu["math"]],reverse = True)
print(stu["name"],end = " ")
for x in chengji:
    print("%.2f%x",end = " ")
print(f"{pingjun:.2f}")
