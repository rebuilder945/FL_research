list1=eval(input())
ini=0
while len(list1)!=0:
    a=list1[0]
    test1=0
    test2=0
    for x in list1:
        if x>a:
            a=x
            test2=test1
        test1+=1
    ini=ini*10+a
    del list1[test2]
print(ini)
