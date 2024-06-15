ls1 = input().split(",")
ls2 = input().split(",")

ls4 = []
for i in range(len(ls1)):
    ls3 = []
    ls3.append(ls1[i])
    ls3.append(ls2[i])
    ls4.append(ls3)
print(sorted(ls4,key=function))
