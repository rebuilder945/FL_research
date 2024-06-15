name = eval(input())
ls2 = name.split(",")
a = eval(input())
ls3 = []
for i in range(len(ls2)):
    ls3.append([ls2[i],a[i]])
print(ls3)
