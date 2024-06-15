name=eval(input).split(",")
scores=list(input())
all=[]
for i in range(len(name)):
    sum=[name[i]+scores[i]]
    all.append(sum)
print(all)
