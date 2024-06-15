names=input().split(",")
grades=eval(input())
ls = []
for i in range(len(names)):
    ls.append([names[i],grades[i]])
print(ls)
