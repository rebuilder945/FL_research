name=input().split(",")
name2=name.copy()
grad=list(map(int,input().split(",")))
grad2=grad.copy()
grad.sort()
for i in range(len(name)):
    name2[i]=name[grad2.index(grad[i])]
lst=[0]*len(name)
for i in range(0,len(name)):
        lst[i]=[name2[i],grad[i]]
print(lst)
