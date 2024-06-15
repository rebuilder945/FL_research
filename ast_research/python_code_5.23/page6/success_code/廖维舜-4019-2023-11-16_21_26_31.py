x=eval(input())
list=[]
for x in x:
    list.append(x)
for x in list[0:]:
    list[x]=int((list[x]+5)%10)
for x in len(list) :
    list[x]=list[-(x+1)]
print(list)

