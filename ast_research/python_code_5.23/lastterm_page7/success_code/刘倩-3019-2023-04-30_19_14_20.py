stu = {"name":input(),"english":eval(input()),"python":eval(input()),"math":eval(input())}

pingjun = (stu["english"] + stu["python"] + stu["math"])/3
stu["avg"] = pingjun
chengji = [stu["english"],stu["python"],stu["math"]].sorted(reverse = True)
print(stu["name"],end = " ")
for x in chengji:
    print(f"{x:.2f}",end = " ")
print(f"{pingjun:.2f}")
