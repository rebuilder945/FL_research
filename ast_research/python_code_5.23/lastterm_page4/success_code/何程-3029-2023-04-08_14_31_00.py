names=input().spilt(",")
scores=eval(input())
r=[]
for i in range(len(names)):
    r.append([names[i],scores[i]])
print(r)
