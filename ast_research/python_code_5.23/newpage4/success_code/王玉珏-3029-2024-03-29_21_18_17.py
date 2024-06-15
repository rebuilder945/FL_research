a=input().split(",")
names=list((a))
b=input()
scores=list(eval(b))
scores=list(eval(b))
resultlist=[]
for name,score in zip(names,scores):
    resultlist.append([name,score])

print(resultlist)
