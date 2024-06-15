n=eval(input())
list1=[]
for x in n:
    list1.append(x)
    list1.sort(reverse=True)
print(*list1,sep="")
