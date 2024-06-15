names=input().split(',')
scores=input().split(',')
l=[]
for i in range(len(names)):
    l.append([names[i]]+[eval(scores[i])])
l.sort(key=lambda x:x[1])
print(l)
