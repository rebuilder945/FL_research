name=input().split(',')
score=eval(input())
new=[]
pos=0
for i in name:
    new.append([i,score[pos]])
    pos+=1
print(new)

