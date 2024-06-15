list1=eval(input())
a=0
while len(list1)!=0:
    b=list1[0]
    d=0
    c=0
    for x in list1:
        if x>b:
            b=x
            c=d
        d+=1
    a=a*10+b
    del list1[c]
print(a)



