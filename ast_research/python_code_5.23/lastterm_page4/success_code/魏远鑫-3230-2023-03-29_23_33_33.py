list=eval(input())
c=list.sort()
b=list.count(0)
for i in range(1,len(list)+b):
    a=list[-i]
    print(a,end="")

