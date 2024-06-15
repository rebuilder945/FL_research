name = eval(input())
ls2 = name.split(",")
grade = eval(input())
ls = []
for i in range(len(ls2)):
    ls.append([ls2[i],ls[i]])
print(ls)
