names=input().split(",")
scores=input().split(",")
long=len(names)
final=[]
for i in range(0,long):
    lst=[]
    lst.append(names[i])
    lst.append(eval(scores[i]))
    final.append(lst)
final.sort(key=lambda x:x[1])
print(final)
