names = input().split(",")
grades = list(map(eval,input().split(",")))
lst=[]
for i in range(len(names)):
    lst.append([names[i],grades[i]])
lst.sort(key=lambda x:x[1])
print(lst)

