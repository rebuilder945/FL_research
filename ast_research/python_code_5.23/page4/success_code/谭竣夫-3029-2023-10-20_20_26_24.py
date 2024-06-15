names=input().split(",")
grades=eval(input())
a=[]
for i in range(len(names)):
    b=[]
    b.append(names[i])
    b.append(grades[i])
    a.append(b)
print(a)
