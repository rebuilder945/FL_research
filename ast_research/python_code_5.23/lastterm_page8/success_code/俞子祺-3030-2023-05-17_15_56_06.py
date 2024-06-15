name=input().split(",")
score=eval(input())
ls1=[[a,b] for a,b in zip(name,score)]
ls1.sorted(key=score)
print(ls1)
