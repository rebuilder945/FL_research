name=input().split(',')
score=eval(input())
new=[]
a=0
for x in name:
    new.append([x,score[a]])
    a+=1
print(new)
