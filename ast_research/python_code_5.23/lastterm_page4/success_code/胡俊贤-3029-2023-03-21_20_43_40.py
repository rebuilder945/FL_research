name=str(input())
names=name.split(",")
scores=evla(input())
n=len(names)
ls=[list(i) for i in zip(names,scores)]
print(ls)

