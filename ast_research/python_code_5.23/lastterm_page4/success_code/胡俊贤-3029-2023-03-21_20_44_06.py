name=str(input())
names=name.split(",")
scores=eval(input())
n=len(names)
ls=[list(i) for i in zip(names,scores)]
print(ls)

