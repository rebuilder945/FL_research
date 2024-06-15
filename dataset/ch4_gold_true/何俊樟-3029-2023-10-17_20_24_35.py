name=input().split(",")
age=eval(input())
all=[]
c=0
for x in name:
    b=[x,age[c]]
    all.append(b)
    c+=1
print(all)

