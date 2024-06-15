l1=list(map(str,input().split(",")))
l2=eval(input())
l3=[]
for x in range(len(l1)):
    l3.append([l1[x],l2[x]])
print(l3)
