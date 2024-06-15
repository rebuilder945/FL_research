names=input().split(",")
scores=eval(input())
a=[]
for x in range(len(names)):
    a.append([names[x],scores[x]])
print(a)


