name=input().split(",")
point=eval(input())
newlist=[[name[i],point[i]] for i in range(len(name))]
print(newlist)
