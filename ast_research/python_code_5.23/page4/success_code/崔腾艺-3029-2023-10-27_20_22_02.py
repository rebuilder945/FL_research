names=input().split(",")
grades=eval(input())
b=[]
for i in range(len(names)):
    a=[names[i],grades[i]]
    b.append(a)
print(b)
