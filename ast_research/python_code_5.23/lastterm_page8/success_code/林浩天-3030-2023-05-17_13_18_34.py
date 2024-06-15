names=input().split(",")
scores=input().split(",")
lis=[]
for n,s in zip(names,scores):
    lis.append([n,s])
students_sorted=sorted(lis,key=lambda x:x[1])
print(students_sorted)
