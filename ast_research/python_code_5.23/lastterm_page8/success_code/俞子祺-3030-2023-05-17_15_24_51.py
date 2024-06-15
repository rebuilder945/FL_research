name=input().split(",")
score=eval(input())
ls1=[]
m=str()
for a in name:
    for b in score:
        m=(a,b)
        ls1.append(m)
        ls1.sort()
print(ls1)
