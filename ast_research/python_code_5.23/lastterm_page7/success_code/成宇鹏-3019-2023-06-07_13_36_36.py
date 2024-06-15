stu = {}
ls1=["name","english","python","math"]
ls2 =input().split()
ls3 = []
for x in range(len(ls1)):
    if x == 0:
        stu[ls1[x]] = ls2[x]
    else:
        i = int(ls2[x])
        ls3.append(i)
        stu[ls1[x]] = i
ave = sum(ls3)/len(ls3)
stu["avg"] = ave
a = stu.pop("name")
c = stu.pop("avg")
b = list(stu.values())
b.sort(reverse = True)
print("%s %.2f %.2f %.2f %.2f"%(a,b[0],b[1],b[2],c))
