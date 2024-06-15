names=input().split(',')
scores=eval(input())
lb=[]
for i in range(len(names)):
    lb.append([names[i],scores[i]])
print(lb)
