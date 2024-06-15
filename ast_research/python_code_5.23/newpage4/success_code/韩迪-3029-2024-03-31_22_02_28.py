INAME=input().split(",")
ISCORE=eval(input())
Is=[]
for i in range(len(INAME)):
    Is.append([INAME[i],ISCORE[i]])
Is.sort(key=lambda X:X[1])
print(Is)

