name=input().split(",")
grad=list(map(int,input().split(",")))
lst=[0]*len(name)
for i in range(0,len(name)):
    if grad[i]<grad[i-1]:
        lst[i-1]=[name[i],grad[i]]
        lst[i]=[name[i-1],grad[i-1]]
    else:
        lst[i]=[name[i],grad[i]]
print(lst)
