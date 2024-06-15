name=input().split(",")
grad=list(map(int,input().split(",")))
grad2=grad.copy()
grad.sort()
for i in range(3):
    name[grad2.index(grad2[i])]=name[grad.index( grad[i])]
lst=[0]*len(name)
for i in range(0,len(name)):
        lst[i]=[name[i],grad[i]]
print(lst)
