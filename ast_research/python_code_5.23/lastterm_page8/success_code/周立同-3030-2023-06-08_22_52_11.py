name=input().split(",")
grad=list(map(int,input().split(",")))
lst=[0]*len(name)
for i in range(0,len(name)):
    lst[i]=[name[i],grad[i]]
print(lst)
