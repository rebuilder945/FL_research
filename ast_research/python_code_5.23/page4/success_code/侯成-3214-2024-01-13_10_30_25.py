list1=eval(input())
test1=0
test2=0
for x in list1:
    if x==0:
        list1[test2]="a"
        test1+=1
    test2+=1
while test1>0:
    list1.remove("a")
    list1.append(0)
    test1-=1
print(list1)
