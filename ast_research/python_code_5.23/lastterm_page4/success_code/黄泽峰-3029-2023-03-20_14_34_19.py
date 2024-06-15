ls1 = input().split(",")
ls2 = eval(input())
ls3=[]
for i in range(len(ls1)):
    ls3.append([str(ls1[i]),int(ls2[i])])
print(ls3)
