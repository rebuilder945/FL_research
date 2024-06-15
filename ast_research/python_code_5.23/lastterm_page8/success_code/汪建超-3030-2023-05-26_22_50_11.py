name = input().split(",")
score = input().split(",")
lst = []
i = 0
for x in name:
    lst.append([x,eval(score[i])])
    i+=1
print(sorted(lst,key = lambda x:(x[1],x[0])))
