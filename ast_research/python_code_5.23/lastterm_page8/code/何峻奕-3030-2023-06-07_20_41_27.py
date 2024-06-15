names=input().split(",")
grades=input().split(",")
for i in range(len(names)):
    t=list(dict(names[i]=grades[i]))
    print(t)

