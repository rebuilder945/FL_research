names=list(input().split(","))
scores=eval(input())
num=len(scores)
for i in range(num):
    lst=[]
    lst.append(names[i])
    lst.append(scores[i])
    print(lst)
