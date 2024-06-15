names=input().split(",")
grade=eval(input())
result=[]
for i in range(len(names)):
    result.append([names[i],grade[i]])
print(result)
