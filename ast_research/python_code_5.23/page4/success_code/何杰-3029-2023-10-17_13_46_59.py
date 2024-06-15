names=input().split(",")
grades=eval(input())
b=[]
i=0
while i<len(grades):
    a=[]
    a.append(names[i])
    a.append(grades[i])
    b.append(a)
    i+=1
print(b)
