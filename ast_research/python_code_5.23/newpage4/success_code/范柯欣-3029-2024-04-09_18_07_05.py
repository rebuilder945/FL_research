name=input().split(",")
scores = list(map(int, input().split(',')))
z=[]
for i in range (len(name)):
    z.append([name[i],scores[i]])
print()
