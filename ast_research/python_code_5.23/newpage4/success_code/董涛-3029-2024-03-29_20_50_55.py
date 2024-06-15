names=input().split(",")
scores=eval(input())
m=[]
for x in range(len(names)):
    m.append([names[x],scores[x]])
print(m)
