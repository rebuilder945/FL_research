names=list(input().split(","))
scores=eval(input())
re=[]
for i in range(len(names)):
    re.append([names[i],scores[i]])
print(re)

