names=input().split(",")
grade=eval(input())
f=[]
for i in range(len(grade)):
    f.append([names[i],grade[i]])
f.sort(key=lambda x:[1])
print(f)
