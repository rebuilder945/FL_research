names=input().split(",")
scores=eval(input())
r=[]
for x in range(len(names)):
    r.append([names[x],scores[x]])
print(r)
