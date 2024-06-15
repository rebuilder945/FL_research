names=input().split(',')
scores=input().split(',')
a=[]
for i in range(len(names)):
    a.append([names[i],int(scores[i])])
a.sort(key=lambda x:x[1])
print(a)

