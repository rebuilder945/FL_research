name = input().split(",")
score = input().split(",")
lst = []
for x in name:
    for i in score:
        lst.append([x,i])
print(sorted(lst,key = lambda x:(x[1],x[0])))
