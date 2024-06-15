name=list(input().split(","))
score=list(eval(input()))
a=[]
for i in range(len(name)):
    b=[]
    b.append(name[i])
    b.append(score[i])
    a.append(b)
print(a)
